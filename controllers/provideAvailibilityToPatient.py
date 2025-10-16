from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User

provideAvailibilityToPatient = Blueprint('provideAvailibilityToPatient', __name__)
@provideAvailibilityToPatient.route("/dashboard/patient/<string:specialization>/<string:fullname>/<string:username>/availibility", methods=['GET','POST'])
def provideAvailibilityToThePatient(specialization,fullname,username):
    print(specialization,fullname,username)
    return render_template("showDoctorAvailibilityToPatient.html")