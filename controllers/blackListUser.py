from datetime import datetime
from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User , BlackListUser

theBlackListingUser = Blueprint('theblacklistinguser', __name__)
@theBlackListingUser.route("/blacklist/<int:id>", methods=['GET','POST'])
def blackListUser(id):
    if('user' in session and session['role']=="admin"):
        user = User.query.filter_by(id=id).first_or_404()
        
        # Check if already blacklisted
        existing_blacklist = BlackListUser.query.filter_by(username=user.username).first()
        if existing_blacklist:
            print(f"User {user.username} is already blacklisted.")
            return redirect("/dashboard/admin")
        
        user.status = -1 
        blacklist = BlackListUser(userid=user.id, username=user.username, role=user.role, reason="Violated terms of service", created_at=datetime.utcnow())
        db.session.add(blacklist)
        db.session.commit()        
        print(f"User with ID {id} has been blacklisted.")
        return redirect("/dashboard/admin")
    else:
        return redirect("/login")

@theBlackListingUser.route("/blacklist-doctor/<int:id>", methods=['GET','POST'])
def blackListDoctor(id):
    if('user' in session and session['role']=="admin"):
        user = User.query.filter_by(id=id).first_or_404()
        
        # Check if already blacklisted
        existing_blacklist = BlackListUser.query.filter_by(username=user.username).first()
        if existing_blacklist:
            print(f"Doctor {user.username} is already blacklisted.")
            return redirect("/dashboard/admin")
        
        user.status = -1 
        blacklist = BlackListUser(userid=user.id, username=user.username, role=user.role, reason="Professional misconduct", created_at=datetime.utcnow())
        db.session.add(blacklist)
        db.session.commit()        
        print(f"Doctor with ID {id} has been blacklisted.")
        return redirect("/dashboard/admin")
    else:
        return redirect("/login")

@theBlackListingUser.route("/blacklistpatient/<int:id>", methods=['GET','POST'])
def blackListPatient(id):
    if('user' in session and session['role']=="admin"):
        user = User.query.filter_by(id=id).first_or_404()
        
        # Check if already blacklisted
        existing_blacklist = BlackListUser.query.filter_by(username=user.username).first()
        if existing_blacklist:
            print(f"Patient {user.username} is already blacklisted.")
            return redirect("/dashboard/admin")
        
        user.status = -1 
        blacklist = BlackListUser(userid=user.id, username=user.username, role=user.role, reason="Inappropriate behavior", created_at=datetime.utcnow())
        db.session.add(blacklist)
        db.session.commit()        
        print(f"Patient with ID {id} has been blacklisted.")
        return redirect("/dashboard/admin")
    else:
        return redirect("/login")