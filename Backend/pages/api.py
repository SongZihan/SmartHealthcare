import jwt
from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash

from application import db
from config.base_setting import SECRET_WORD
from libs.auth import login_required, jwt_login
from libs.date_helper import getCurrentTime
from libs.return_data_helper import ops_renderErrJSON, ops_renderJSON
from libs.wtf_helper import Register, Login
from models.user import User

api = Blueprint("api", __name__)


@api.route('/',methods=["GET"])
def index():
    return 'i get you~'

@api.route('/login',methods=["POST"])
def login():
    print(request.form)
    form = Login()
    if form.validate():
        user = User.query.filter_by(login_name=form.username.data).first()
        # 使用check_password_hash验证用户密码，其中第一个参数是数据库中查询的用户加密密码，第二个参数是用户输入的密码
        if check_password_hash(user._login_pwd, form.password.data):
            # 通过验证的话就使用flask-login想客户端发送cookie
            jwt_token = jwt_login(form)
            # 封装数据库中的token信息到data中
            fibit_token = user.fibit_token
            return ops_renderJSON(msg="login success~~",data=[jwt_token,fibit_token])
        else:
            return ops_renderErrJSON(msg="密码错误")
    else:
        return ops_renderErrJSON(msg=str(form.errors))

@api.route('/register',methods=["POST"])
def register():
    form = Register()
    if form.validate():
        # 将用户信息注册进数据库
        model_user = User()
        model_user.login_name = form.username.data
        # 使用加密方法存储密码
        model_user._login_pwd = generate_password_hash(form.password.data)
        model_user.created_time = model_user.updated_time = getCurrentTime()
        try:
            db.session.add(model_user)
            db.session.commit()
        except Exception as error:
            return ops_renderErrJSON(msg=str(error))
        else:
            return ops_renderJSON(msg="注册成功~~")
    else:
        # 返回表单验证中的错误信息
        return ops_renderErrJSON(msg=str(form.errors))


@api.route('/get_fibit_token',methods=["GET"],endpoint='get_access')
@login_required
def get_data():
    # 解密jwt，获取用户id
    jwt_tokens = request.headers.get('Authorization', default=None).encode('utf-8')
    decode_tokens = jwt.decode(jwt_tokens, SECRET_WORD, algorithms=['HS256'])
    username = decode_tokens['username']
    # 获取请求中的access_token
    token = request.args.get('token').split('=')[1].split('&')[0]

    # 提交token到数据库
    try:
        this_user = User.sbumit_token(token,username)
        db.session.add(this_user)
        db.session.commit()
    except Exception as error:
        return -1, str(error)
    else:
        return 201,"添加成功~~",token

