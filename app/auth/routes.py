from app.auth import auth
from flask import render_template,url_for,request,session,redirect


@auth.route('/presignup')
def presignup():
    return render_template('pre_signup.html')

@auth.route('/prelogin')
def prelogin():
    return render_template('pre_login.html')

@auth.route("/logout")
def clear_session():
    session.clear()
    return redirect("https://rrts-login.onrender.com")

    # return redirect(url_for("home"))