from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User

thelogin = Blueprint('thelogin', __name__)
@thelogin.route("/login", methods=['GET','POST'])
def login():
    print("Login Page")
    if(request.method=="POST"):
        username=request.form.get("username")
        password=request.form.get("password")

        user=User.query.filter_by(username=username,password=password).first()
        if(user):
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
            return render_template("invalid.html")
    return render_template("login.html")