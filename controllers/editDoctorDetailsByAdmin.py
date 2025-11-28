from flask import Flask,render_template,redirect,request,Response,Blueprint,session,url_for
from database import db
from models.models import User,Doctor

theeditdoctordetailsbyadmin = Blueprint('theeditdoctordetailsbyadmin', __name__)
@theeditdoctordetailsbyadmin.route("/edit-doctor/<int:id>", methods=['GET','POST'])
def EditDoctorDetailsByAdmin(id):
    print("i am being called ", id )
    if('user' in session):
        docusername= User.query.filter_by(id=id, role="doctor").first().username
        print("Doctor username to edit:", docusername)
        
        doctor = Doctor.query.filter_by(username=docusername).first_or_404()
    if request.method == "POST":
        doctor.fullname = request.form['fullname']
        doctor.specialization = request.form['specialization']
        doctor.phone = request.form['phone']
        doctor.email = request.form['email']
        doctor.address = request.form['address']
        db.session.commit()
        return redirect("/dashboard/admin")
    return render_template("editDoctorDetailsByAdmin.html", doctor=doctor)