from flask import Flask,render_template,redirect,request,Response,Blueprint,session,url_for
from database import db
from models.models import User,Patient

theeditpatientdetailsByAdmin = Blueprint('theeditpatientdetailsByAdmin', __name__)
@theeditpatientdetailsByAdmin.route("/admin/edit-patient/<string:username>", methods=['GET','POST'])
def EditPatientDetailsByAdmin(username):

    if('user' in session):
  
        patientuserid= User.query.filter_by(username=username, role="patient").first().id
        print("Patient username to edit:", patientuserid)
        
        patient = Patient.query.filter_by(userid=patientuserid).first_or_404()
    if request.method == "POST":
        patient.name = request.form['name']
        patient.dob = request.form['dob']
        patient.phone = request.form['phone']
        patient.email = request.form['email']
        patient.address = request.form['address']
        patient.emergencycontact = request.form['emergencycontact']
        db.session.commit()
        return redirect("/dashboard/admin")
    return render_template("editPatientDetailsByAdmin.html", patient=patient)