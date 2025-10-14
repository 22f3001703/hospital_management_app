from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User

registertheDoctor = Blueprint('registertheDoctor', __name__)
@registertheDoctor.route("/dashboard/admin/register-doctor", methods=['GET','POST'])
def registerDoctor():
    return render_template("registerDoctor.html")