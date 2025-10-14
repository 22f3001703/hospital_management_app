from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User
from models.models import Doctor

registertheDoctor = Blueprint('registertheDoctor', __name__)
@registertheDoctor.route("/dashboard/admin/register-doctor", methods=['GET','POST'])
def registerDoctor():
    if('user' in session and session['role']=="admin"):
        print("Registering the Doctor")
        if(request.method=="POST"):
            fullname=request.form.get("fullname")
            address=request.form.get("address")
            phone=request.form.get("phone")
            email=request.form.get("email")
            username=request.form.get("username")
            password=request.form.get("password")
            experience=request.form.get("experience")
            specialization=request.form.get("specialization")

            new_doctor=Doctor(fullname=fullname,address=address,phone=phone,email=email,username=username,password=password,experience=experience,specialization=specialization)
            db.session.add(new_doctor)
            db.session.commit()
            print("Doctor registered successfully")
            new_user=User(fullname=fullname,username=username,password=password,role="doctor",status=0)
            db.session.add(new_user)
            db.session.commit()
            print("User as a Doctor registered successfully")
            return redirect("/dashboard/admin")
    return render_template("registerDoctor.html")