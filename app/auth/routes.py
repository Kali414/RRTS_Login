from app.auth import auth
from flask import render_template,url_for,request


@auth.route('/presignup')
def presignup():
    return render_template('pre_signup.html')

@auth.route('/prelogin')
def prelogin():
    return render_template('pre_login.html')