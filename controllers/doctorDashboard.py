from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User,Appointments

thedoctorDashboard = Blueprint('thedoctorDashboard', __name__)
@thedoctorDashboard.route("/dashboard/doctor", methods=['GET','POST'])
def doctorDashboard():
    if('user' in session and session['role']=="doctor"):
        user=session['user']
        allapointments= Appointments.query.filter_by(doctor=user).all()
        print("All Appointments for Doctor:", allapointments)
        appointment=[]
        innerdetails={}
        for x in allapointments:
            getpatientdetails=User.query.filter_by(username=x.patient).first()
            if(x.status=="booked"):
                innerdetails={
                    "id": x.id,
                    "fullname": getpatientdetails.fullname,
                    "date": x.date,
                    "timeslot": x.timeslot,
                    "status": x.status,
                    "username": getpatientdetails.username

                }
            if not innerdetails:
                continue
            appointment.append(innerdetails)
        print(appointment)    
        assignedpatients=Appointments.query.filter_by(doctor=user, status="booked").all()
        finalassignedpatients=[]
        innerpatientdetails={}
        print("Assigned Patients:", assignedpatients)
        for y in assignedpatients:
            getassignedpatientdetails=User.query.filter_by(username=y.patient).first()
            innerpatientdetails={
                "id": y.id,
                "fullname": getassignedpatientdetails.fullname,
                "username": getassignedpatientdetails.username,        
            }
            finalassignedpatients.append(innerpatientdetails)
            print(y.patient)
        return render_template("doctorDashboard.html",user=user, appointment=appointment,finalassignedpatients=finalassignedpatients)
    else:
        return redirect("/login")