from flask import render_template,url_for,request,redirect,session

from app import app

@app.route('/')
def home():
    return render_template('home.html')


@app.route("/report_issue", methods=["GET", "POST"])
def report_issue():
    if not session.get("name"):
        return redirect(url_for("auth.prelogin"))
        
    if request.method == "GET" :
        return render_template("report_issue.html")

    return render_template("report_issue.html")

@app.route("/track-repair")
def track_repair():
    if not session.get("name"):
        return redirect(url_for("auth.prelogin"))

    return render_template("track_repair.html")




@app.route("/contact",methods=["GET","POST"])
def contact():
    return render_template("contact.html")