from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User,Appointments

theActionWithAppointment = Blueprint('theactionwithappointment', __name__)
@theActionWithAppointment.route("/dashboard/patient/action-on-appointment/<int:appointment_id>/<string:action>", methods=['GET','POST'])
def actionToAppointment(appointment_id, action):

    print("Canceling of Appointment Started")
    print(action)
    appointment = Appointments.query.filter_by(id=appointment_id).first()
    print("Fetched Appointment:", appointment)
    if appointment:
        print("Updating appointment status to:", action)
        appointment.status = action
        db.session.commit()
        print("Appointment status updated successfully")
    return redirect("/dashboard/doctor")