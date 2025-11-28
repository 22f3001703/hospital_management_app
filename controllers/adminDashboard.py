from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User, Patient
from models.models import Doctor , Appointments

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
        allappointment= Appointments.query.all()
        print(allappointment)
        allappointments=[]
        innerdetails={}
        for appointment in allappointment:
            patient=User.query.filter_by(username=appointment.patient).first()
            doctor=User.query.filter_by(username=appointment.doctor).first()
            department = Doctor.query.filter_by(username=appointment.doctor).first().specialization
            if(appointment.status=="booked"):
                innerdetails={
                    'id':appointment.id,      
                    'patient_fullname':patient.fullname,
                    'doctor_fullname':doctor.fullname,
                    'department':department,    
                    'date':appointment.date,
                    'timeslot':appointment.timeslot,
                    'status':appointment.status,
                    'pt_username':appointment.patient,
                }
                allappointments.append(innerdetails)

        
        return render_template("adminDashboard.html",user=user , alldoctors=alldoctors, doctdetails=doctdetails, allpatients=allpatients, patientdetails=patientdetails , allappointments=allappointments)
    else:
        return redirect("/login")