from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User

thepatientDashboard = Blueprint('thepatientDashboard', __name__)
@thepatientDashboard.route("/dashboard/patient", methods=['GET','POST'])
def patientDashboard():
    if('user' in session and session['role']=="patient"):
        user=session['user']
        return render_template("patientDashboard.html",user=user)
    else:
        return redirect("/login")