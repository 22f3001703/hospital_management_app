from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User,Appointments , Doctor

thedeleteDoctor = Blueprint('thedeleteDoctor', __name__)
@thedeleteDoctor.route("/delete/<int:id>", methods=['GET','POST'])
def deleteDoctor(id):
    if('user' in session and session['role']=="admin"):
        #doctor = Doctor.query.filter_by(id=id).first_or_404()
        user = User.query.filter_by(id=id).first_or_404()
        user.status = 0  
        db.session.commit()        
        print(f"User with ID {id} and associated user account have been deleted.")
        return redirect("/dashboard/admin")
    else:
        return redirect("/login")