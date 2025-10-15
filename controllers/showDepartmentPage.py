from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User

showthedepartment = Blueprint('showthedepartment', __name__)
@showthedepartment.route("/dashboard/patient/dep-details/<string:depname>", methods=['GET','POST'])
def showTheDepartment(depname):
    print(depname)
    return render_template("departmentPage.html",depname=depname)
