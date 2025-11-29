from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User , Patient

registerthePatient = Blueprint('registerthePatient', __name__)
@registerthePatient.route("/register", methods=['GET','POST'])
def registerPatient():
    print("Registering Patient")
    if(request.method=="POST"):
        fullname=request.form.get("fullname")
        username=request.form.get("username")
        password=request.form.get("password")
        role="patient"

        IsUsernameExsist=User.query.filter_by(username=username).first()
        if(IsUsernameExsist):
            return render_template("duplicate.html")
        else:
            new_patient = User(fullname=fullname,username=username,password=password,role=role,status=0)
            db.session.add(new_patient)
            db.session.commit()
            new_patient_id = new_patient.id
            pat = Patient(userid=new_patient_id,name=fullname,dob="",phone="",email="",address="",emergencycontact="")
            db.session.add(pat) 
            db.session.commit()
            print("Patient Registration Done🤷🏻‍♀️")
            return redirect("/login")
    return render_template("register.html")     


