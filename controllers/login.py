from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User, BlackListUser

thelogin = Blueprint('thelogin', __name__)
@thelogin.route("/login", methods=['GET','POST'])
def login():
    print("Login Page")
    if(request.method=="POST"):
        username=request.form.get("username")
        password=request.form.get("password")

        user=User.query.filter_by(username=username,password=password).first()
        
        # Check if user exists and credentials are correct
        if not user:
            message="Invalid username or password. Please try again."
            return render_template("invalid.html", message=message)
        
        # Check if user is blacklisted
        blacklisted = BlackListUser.query.filter_by(username=username).first()
        if blacklisted:
            message=f"Your account has been blacklisted. Reason: {blacklisted.reason}. Please contact admin for more information."
            return render_template("invalid.html", message=message)
        
        # Check if user status is blocked (status = -1)
        if user.status == -1:
            message="Your account has been suspended. Please contact admin for assistance."
            return render_template("invalid.html", message=message)
        
        print(user.status)
        print("after this")
        if(user.status==1):
            user.status=1
            db.session.commit()
            session['id']=user.id
            session['user']=user.username
            session['role']=user.role
            session['status']=user.status
            print(session)
            if(user.role=="admin"):
                return redirect("/dashboard/admin")     
            elif(user.role=="patient"):
                return redirect("/dashboard/patient")
            elif(user.role=="doctor"):
                return redirect("/dashboard/doctor")
        else:
            message="Sorry , You have been removed from the system or invalid credentials, please contact admin."
            return render_template("invalid.html", message=message)
    return render_template("login.html")