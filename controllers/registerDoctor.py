from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User, Doctor, BlackListUser, Department

registertheDoctor = Blueprint('registertheDoctor', __name__)
@registertheDoctor.route("/dashboard/admin/register-doctor", methods=['GET','POST'])
def registerDoctor():
    if('user' in session and session['role']=="admin"):
        print("Registering the Doctor")
        
        # Get all existing departments for dropdown
        departments = Department.query.all()
        
        if(request.method=="POST"):
            fullname=request.form.get("fullname")
            address=request.form.get("address")
            phone=request.form.get("phone")
            email=request.form.get("email")
            username=request.form.get("username")
            password=request.form.get("password")
            experience=request.form.get("experience")
            
            # Handle department/specialization
            dept_choice = request.form.get("dept_choice")
            if dept_choice == "existing":
                specialization = request.form.get("existing_specialization")
            elif dept_choice == "new":
                new_dept_name = request.form.get("new_dept_name").strip()
                new_dept_description = request.form.get("new_dept_description").strip()
                
                # Check if department already exists
                existing_dept = Department.query.filter_by(name=new_dept_name).first()
                if not existing_dept:
                    # Create new department
                    new_department = Department(name=new_dept_name, descreption=new_dept_description)
                    db.session.add(new_department)
                    db.session.commit()
                
                specialization = new_dept_name
            else:
                # Fallback to manual entry
                specialization = request.form.get("manual_specialization")

            # Check if username already exists
            IsUsernameExsist=User.query.filter_by(username=username).first()
            if(IsUsernameExsist):
                message="Username already exists. Please choose a different username."
                return render_template("invalid.html", message=message)
            
            # Check if username is blacklisted
            isBlacklisted = BlackListUser.query.filter_by(username=username).first()
            if(isBlacklisted):
                message=f"This username has been blacklisted and cannot be used. Reason: {isBlacklisted.reason}. Please choose a different username."
                return render_template("invalid.html", message=message)

            new_doctor=Doctor(fullname=fullname,address=address,phone=phone,email=email,username=username,password=password,experience=experience,specialization=specialization)
            db.session.add(new_doctor)
            db.session.commit()
            print("Doctor registered successfully")
            new_user=User(fullname=fullname,username=username,password=password,role="doctor",status=1)
            db.session.add(new_user)
            db.session.commit()
            print("User as a Doctor registered successfully")
            return redirect("/dashboard/admin")
    
        return render_template("registerDoctor.html", departments=departments)
    else:
        return redirect("/login")