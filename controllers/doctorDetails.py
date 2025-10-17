from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User,Doctor
from models.models import Department

thedoctorDetails = Blueprint('thedoctorDetails', __name__)
@thedoctorDetails.route("/dashboard/patient/dep-details/<string:specialization>/<string:username>", methods=['GET','POST'])
def doctorDetails(username,specialization):
    print(username)
    print(specialization)
    getDoctorDetails=Doctor.query.filter_by(username=username).first()
    print(getDoctorDetails)
    print(getDoctorDetails.fullname)
    return render_template("doctorDetails.html",getDoctorDetails=getDoctorDetails)