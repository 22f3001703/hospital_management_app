from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User,Appointments,Treatment, Doctor
thePatientHistory = Blueprint('thepatienthistory', __name__)
@thePatientHistory.route("/dashboard/patient-history/<string:pt_username>", methods=['GET','POST'])
def patientHistory(pt_username):
    if('user' in session):
        user=session['user']
        role=session['role']
        print(user)
        pt_name= User.query.filter_by(username=pt_username).first().fullname

            
        appointments=Appointments.query.filter_by(patient=pt_username).all()
        allrelevantrecordsid=[]
        for x in appointments:
            if(x.status=="completed"):
                allrelevantrecordsid.append(x.id)
        innerrecorddetails={}
        sendabletreatmentrecords=[]        
        for i in range(len(allrelevantrecordsid)):
            print("Appointment IDs:", allrelevantrecordsid[i])
            Treatmentrecord=Treatment.query.filter_by(appointmentid=allrelevantrecordsid[i]).first()
            print("Treatment Record Fetched:", Treatmentrecord)
            appointfordoctor = Appointments.query.filter_by(id=allrelevantrecordsid[i]).first()
            doctorusername=appointfordoctor.doctor
            doctordetails=Doctor.query.filter_by(username=doctorusername).first()
            doctorname=doctordetails.fullname
            department=doctordetails.specialization
            print("Department for Appointment ID", allrelevantrecordsid[i], "is", department)
            innerrecorddetails={
                "department": department,
                "doctorname": doctorname,
                "appointment_id": Treatmentrecord.appointmentid,
                "diagnosis": Treatmentrecord.diagnosis,
                "prescription": Treatmentrecord.prescreption,
                "medicines": Treatmentrecord.medicines,
                "notes": Treatmentrecord.notes,
                "test": Treatmentrecord.test,
                "visittype": Treatmentrecord.visittype
            }
            print("Inner Record Details:", innerrecorddetails)
            sendabletreatmentrecords.append(innerrecorddetails)
        print("All Treatment Records:", sendabletreatmentrecords)

        return render_template("patientHistory.html",user=user ,sendabletreatmentrecords=sendabletreatmentrecords,pt_name=pt_name,appointments=appointments, patient_username=pt_username, allrelevantrecordsid=allrelevantrecordsid)
    else:
        return redirect("/login")