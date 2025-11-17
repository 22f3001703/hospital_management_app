from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User, Patient
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
        allpatients=User.query.filter_by(role="patient").all()
        print(allpatients)
        patientdetails= Patient.query.all()
        print(patientdetails)
        for x in patientdetails:
            print(x.email)
        
        return render_template("adminDashboard.html",user=user , alldoctors=alldoctors, doctdetails=doctdetails, allpatients=allpatients, patientdetails=patientdetails)
    else:
        return redirect("/login")