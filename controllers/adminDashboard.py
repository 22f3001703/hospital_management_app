from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User

theadminDashboard = Blueprint('theadminDashboard', __name__)
@theadminDashboard.route("/dashboard/admin", methods=['GET','POST'])
def adminDashboard():
    if('user' in session and session['role']=="admin"):
        user=session['user']
        return render_template("adminDashboard.html",user=user)
    else:
        return redirect("/login")