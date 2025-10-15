from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User
from models.models import Department

thepatientDashboard = Blueprint('thepatientDashboard', __name__)
@thepatientDashboard.route("/dashboard/patient", methods=['GET','POST'])
def patientDashboard():
    if('user' in session and session['role']=="patient"):
        user=session['user']
        ##to bring list of departemnts
        departments= Department.query.all()

        return render_template("patientDashboard.html",user=user, departments=departments)
    

    else:
        return redirect("/login")