from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User

thedoctorDashboard = Blueprint('thedoctorDashboard', __name__)
@thedoctorDashboard.route("/dashboard/doctor", methods=['GET','POST'])
def doctorDashboard():
    if('user' in session and session['role']=="doctor"):
        user=session['user']
        return render_template("doctorDashboard.html",user=user)
    else:
        return redirect("/login")