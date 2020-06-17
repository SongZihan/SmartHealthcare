from application import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(25), nullable=False, unique=True)
    _login_pwd = db.Column(db.String(150), nullable=False)
    fibit_token = db.Column(db.String(300), nullable=True)
    status = db.Column(db.Integer, nullable=False, server_default="1")
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

    @staticmethod
    def sbumit_token(token,username):
        # 获取用户对象
        this_user = User.query.filter_by(login_name=username).first()
        # 添加token
        this_user.fibit_token = token

        return this_user


# db.create_all()
