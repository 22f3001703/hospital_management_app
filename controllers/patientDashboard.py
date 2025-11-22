from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User
from models.models import Department , Appointments

thepatientDashboard = Blueprint('thepatientDashboard', __name__)
@thepatientDashboard.route("/dashboard/patient", methods=['GET','POST'])
def patientDashboard():
    if('user' in session and session['role']=="patient"):
        user=session['user']
        departments= Department.query.all()

        myappointmnets= Appointments.query.filter_by(patient=user).all()
        print("My Appointments:", myappointmnets)

        return render_template("patientDashboard.html",user=user, departments=departments, myappointmnets=myappointmnets)
    
    
    else:
        return redirect("/login")