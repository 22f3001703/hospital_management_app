from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User

theAppointmentBooking = Blueprint('theappointmentbook', __name__)
@theAppointmentBooking.route("/dashboard/patient/<string:specialization>/<string:fullname>/<string:username>/availibility/book", methods=['GET','POST'])
def BookAppointment(specialization, fullname, username):
    print("Book Appointment Page")
    print(session['user'])
    print(specialization, fullname, username)
    return redirect("/dashboard/patient")