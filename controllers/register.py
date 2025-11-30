from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User , Patient, BlackListUser

registerthePatient = Blueprint('registerthePatient', __name__)
@registerthePatient.route("/register", methods=['GET','POST'])
def registerPatient():
    print("Registering Patient")
    if(request.method=="POST"):
        fullname=request.form.get("fullname")
        username=request.form.get("username")
        password=request.form.get("password")
        role="patient"
        isBlacklisted = BlackListUser.query.filter_by(username=username).first()
        IsUsernameExsist=User.query.filter_by(username=username).first()    

        
        if(isBlacklisted):
            message=f"This username has been blacklisted and cannot be used. Reason: {isBlacklisted.reason}. Please choose a different username."
            return render_template("invalid.html", message=message)
        else:
            if(IsUsernameExsist):
                return render_template("duplicate.html")
            new_patient = User(fullname=fullname,username=username,password=password,role=role,status=1)
            db.session.add(new_patient)
            db.session.commit()
            new_patient_id = new_patient.id
            pat = Patient(userid=new_patient_id,name=fullname,dob="",phone="",email="",address="",emergencycontact="")
            db.session.add(pat) 
            db.session.commit()
            print("Patient Registration Done🤷🏻‍♀️")
            return redirect("/login")
    return render_template("register.html")     


