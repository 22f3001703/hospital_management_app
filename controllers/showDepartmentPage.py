from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User,Department,Doctor

showthedepartment = Blueprint('showthedepartment', __name__)
@showthedepartment.route("/dashboard/patient/dep-details/<string:depname>", methods=['GET','POST'])
def showTheDepartment(depname):
    print(depname)
    getDetails = Department.query.filter_by(name=depname).first()
    getdoctors = Doctor.query.filter_by(specialization=depname).all()
    print(getdoctors)
    return render_template("departmentPage.html",getDetails=getDetails, getdoctors=getdoctors)
