from datetime import datetime
from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User , BlackListUser

theBlackListingUser = Blueprint('theblacklistinguser', __name__)
@theBlackListingUser.route("/blacklist/<int:id>", methods=['GET','POST'])
def blackListUser(id):
    if('user' in session and session['role']=="admin"):
        user = User.query.filter_by(id=id).first_or_404()
        user.status = -1 
        blacklist =  BlackListUser(userid=user.id, username=user.username, role=user.role, reason="Violated terms of service",created_at=datetime.utcnow())
        db.session.add(blacklist)
        db.session.commit()        
        print(f"User with ID {id} has been blacklisted.")
        return redirect("/dashboard/admin")
    else:
        return redirect("/login")