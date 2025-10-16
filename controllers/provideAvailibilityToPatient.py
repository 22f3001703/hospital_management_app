from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User,DoctorAvailibility
import datetime

provideAvailibilityToPatient = Blueprint('provideAvailibilityToPatient', __name__)
@provideAvailibilityToPatient.route("/dashboard/patient/<string:specialization>/<string:fullname>/<string:username>/availibility", methods=['GET','POST'])
def provideAvailibilityToThePatient(specialization,fullname,username):
    print(specialization,fullname,username)
    currentdate = datetime.date.today()
    docavailibility={}
    next7date=currentdate+datetime.timedelta(days=6)
    getAvailibility = DoctorAvailibility.query.filter(
    DoctorAvailibility.username == username,
    DoctorAvailibility.date>=currentdate,
    DoctorAvailibility.date<=next7date).order_by(DoctorAvailibility.date).all()

    for lol in getAvailibility:
        docavailibility[lol.date]=[lol.time1,lol.time2]
    print(getAvailibility)
    x=docavailibility.keys()
    print(x)
    for al in docavailibility.items():
        print(al[1][0],al[1][1])
    docavailibility = {date.isoformat(): slots for date, slots in docavailibility.items()}
    
    if(len(x)==0):
        return render_template("showDoctorAvailibilityToPatient.html",docavailibility=None,x=x)
    
    return render_template("showDoctorAvailibilityToPatient.html",docavailibility=docavailibility)