from flask import Flask,render_template,redirect,request,Response,Blueprint,session,url_for
from database import db
from models.models import User,Patient

theeditpatientdetails = Blueprint('theeditpatientdetails', __name__)
@theeditpatientdetails.route("/edit-patient/<int:id>", methods=['GET','POST'])
def EditPatientDetails(id):
    if('user' in session):
        patient = Patient.query.filter_by(userid=id).first_or_404()
    if request.method == "POST":
        patient.name = request.form['name']
        patient.dob = request.form['dob']
        patient.phone = request.form['phone']
        patient.email = request.form['email']
        patient.address = request.form['address']
        patient.emergencycontact = request.form['emergencycontact']
        db.session.commit()
        return redirect("/dashboard/patient")
    return render_template("editPatientDetails.html", patient=patient)