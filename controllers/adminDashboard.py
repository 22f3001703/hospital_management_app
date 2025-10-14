from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User
from models.models import Doctor

theadminDashboard = Blueprint('theadminDashboard', __name__)
@theadminDashboard.route("/dashboard/admin", methods=['GET','POST'])
def adminDashboard():
    if('user' in session and session['role']=="admin"):
        user=session['user']
        print(user)
        alldoctors=User.query.filter_by(role="doctor").all()
        print(alldoctors)
        doctdetails= Doctor.query.all()
        print(doctdetails)
        return render_template("adminDashboard.html",user=user , alldoctors=alldoctors, doctdetails=doctdetails)
    else:
        return redirect("/login")