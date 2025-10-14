from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User
from models.models import Doctor
from models.models import DoctorAvailibility
import datetime

provideTheAvailibility = Blueprint('provideTheAvailibility', __name__)
@provideTheAvailibility.route("/doctor/slots", methods=['GET','POST'])
def provideAvailibility():
    print(session["user"])
    username= session['user']
    availibility={}
    currentdate = datetime.date.today()
    j=0
    print(currentdate)
    for i in range(7):
        next7date= currentdate+datetime.timedelta(days=i)
        print(next7date)
        chekavailibility = DoctorAvailibility.query.filter_by(username=username).filter_by(date=next7date).first()
        print(chekavailibility)
        if(chekavailibility):
            j=j+1
        else:
            break
    for x in range(7-j):
            registeravailable=DoctorAvailibility(username=username,date=next7date,time1=0,time2=0)
            db.session.add(registeravailable)
            db.session.commit()
            next7date=next7date+datetime.timedelta(days=1)

    enddate = currentdate + datetime.timedelta(days=6)   
    endresultfordict=DoctorAvailibility.query.filter(
         DoctorAvailibility.username == username,
        DoctorAvailibility.date >= currentdate,
        DoctorAvailibility.date <= enddate).order_by(DoctorAvailibility.date).all()
    
    for entry in endresultfordict:
        availibility[entry.date] = [entry.time1, entry.time2]

    print("Availability Dict:", availibility)    
                                                         
    return render_template("provideAvailibility.html",availibility=availibility)