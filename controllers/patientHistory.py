from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User,Appointments,Treatment, Doctor
thePatientHistory = Blueprint('thepatienthistory', __name__)
@thePatientHistory.route("/dashboard/doctor/patient-history/<string:pt_username>", methods=['GET','POST'])
def patientHistory(pt_username):
    if('user' in session and session['role']=="doctor"):
        user=session['user']
        role=session['role']
        print(user)
        if role=="doctor":
            getdoctor= Doctor.query.filter_by(username=user).first()
            department=getdoctor.specialization
            print("Doctor's Department:", department)
            appointments=Appointments.query.filter_by(patient=pt_username,doctor=user).all()
            allrelevantrecordsid=[]
            for x in appointments:
                if(x.status=="completed"):
                    allrelevantrecordsid.append(x.id)
            for i in range(len(allrelevantrecordsid)):
                print("Appointment IDs:", allrelevantrecordsid[i])
            return render_template("patientHistory.html",user=user , appointments=appointments, patient_username=pt_username,department=department, allrelevantrecordsid=allrelevantrecordsid)
    else:
        return redirect("/login")