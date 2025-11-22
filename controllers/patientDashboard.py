from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import Doctor, User
from models.models import Department , Appointments

thepatientDashboard = Blueprint('thepatientDashboard', __name__)
@thepatientDashboard.route("/dashboard/patient", methods=['GET','POST'])
def patientDashboard():
    if('user' in session and session['role']=="patient"):
        user=session['user']
        departments= Department.query.all()

        myappointmnets= Appointments.query.filter_by(patient=user).all()
        print("My Appointments:", myappointmnets)
        sendabledata = []
        details = {}
        for x in myappointmnets:
            getdoctorsderails=Doctor.query.filter_by(username=x.doctor).first()
            details={
                "id": x.id,
                "fullname": getdoctorsderails.fullname,
                "specialization": getdoctorsderails.specialization,
                "date": x.date,
                "timeslot": x.timeslot,
                "status": x.status
            }
            sendabledata.append(details)
        print("Sendable Data:", sendabledata)

        return render_template("patientDashboard.html",user=user, departments=departments, sendabledata=sendabledata)
    
    
    else:
        return redirect("/login")