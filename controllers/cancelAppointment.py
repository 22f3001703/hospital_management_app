from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User,Appointments

theCancelAppointment = Blueprint('thecancelappointment', __name__)
@theCancelAppointment.route("/dashboard/patient/cancel-appointment/<int:appointment_id>", methods=['GET','POST'])
def CancelAppointment(appointment_id):
    print("Canceling of Appointment Started")
    appointment = Appointments.query.filter_by(id=appointment_id).first()
    if appointment and appointment.patient == session['user']:
        appointment.status = "cancelled"
        db.session.commit()
        print("Appointment cancelled successfully")
    return redirect("/dashboard/patient")