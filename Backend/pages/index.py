from flask import render_template

from application import app, db



@app.route('/',methods=["GET"])
def index():
    return 'i get you~'




