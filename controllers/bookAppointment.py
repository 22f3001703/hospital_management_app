from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User,Appointments

theAppointmentBooking = Blueprint('theappointmentbook', __name__)
@theAppointmentBooking.route("/dashboard/patient/<string:specialization>/<string:fullname>/<string:username>/availibility/book", methods=['GET','POST'])
def BookAppointment(specialization, fullname, username):
    print("Book Appointment Page")
    print(session['user'])
    print(specialization, fullname, username)
    data = request.get_json()

    date = data.get("date")
    timeslot = data.get("timeslot")

    print("Selected Date:", date)
    print("Selected Time Slot:", timeslot)

    new_appointment = Appointments(patient=session['user'], doctor=username, date=date, timeslot=timeslot, status="booked")
    db.session.add(new_appointment)
    db.session.commit()

    return redirect("/dashboard/patient")