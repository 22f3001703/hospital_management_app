from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import Treatment, User,Appointments

theUpdatePatientHistory = Blueprint('theupdatepatienthistory', __name__)
@theUpdatePatientHistory.route("/dashboard/doctor/patient-history/<string:patient_username>/<int:appointment_id>", methods=['GET','POST'])
def UpdatePatientHistory(patient_username, appointment_id):
    if('user' in session and session['role']=="doctor"):
        user=session['user']
        print("Update Patient History Page")
        print("Doctor:", user)
        print("Patient Username:", patient_username)
        print("Appointment ID:", appointment_id)

        if request.method == 'POST':
            diagnosis = request.form.get("diagnosis")
            prescription = request.form.get("prescription")
            medicines = request.form.get("medicines")
            notes = request.form.get("notes")

            print("Diagnosis:", diagnosis)
            print("Prescreption:", prescription)
            print("Medicines:", medicines)
            print("Notes:", notes)

            new_treatment = Treatment(appointmentid=appointment_id, diagnosis=diagnosis, prescreption=prescription, medicines=medicines, notes=notes)
            db.session.add(new_treatment)
            db.session.commit()

            print("Patient history updated successfully")
            return redirect("/dashboard/doctor")

        return render_template("patientHistory.html", user=user, patient_username=patient_username, appointment_id=appointment_id)
    else:
        return redirect("/login")
