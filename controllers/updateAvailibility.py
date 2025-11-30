from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User
from models.models import Doctor
from models.models import DoctorAvailibility
import datetime

updateavailibility = Blueprint('updateavailibility', __name__)
@updateavailibility.route("/availibility/edit/<doctor_username>", methods=['GET','POST'])
def updateDoctorAvailibility(doctor_username):
    if('user' in session and (session['role']=="admin" or (session['role']=="doctor" and session['user']==doctor_username))):

        doctor_user = User.query.filter_by(username=doctor_username, role="doctor").first()
        if not doctor_user:
            return redirect("/dashboard/admin")
        
        doctor_details = Doctor.query.filter_by(username=doctor_username).first()
        

        availibility={}
        currentdate = datetime.date.today()
        j=0
        print(currentdate)
        for i in range(7):
            next7date= currentdate+datetime.timedelta(days=i)
            print(next7date)
            chekavailibility = DoctorAvailibility.query.filter_by(username=doctor_username).filter_by(date=next7date).first()
            print(chekavailibility)
            if(chekavailibility):
                j=j+1
            else:
                break
        for x in range(7-j):
                registeravailable=DoctorAvailibility(username=doctor_username,date=next7date,time1=0,time2=0)
                db.session.add(registeravailable)
                db.session.commit()
                next7date=next7date+datetime.timedelta(days=1)

        enddate = currentdate + datetime.timedelta(days=6)   
        endresultfordict=DoctorAvailibility.query.filter(
             DoctorAvailibility.username == doctor_username,
            DoctorAvailibility.date >= currentdate,
            DoctorAvailibility.date <= enddate).order_by(DoctorAvailibility.date).all()
        
        for entry in endresultfordict:
            availibility[entry.date] = [entry.time1, entry.time2]

        availibility = {date.isoformat(): slots for date, slots in availibility.items()}
        
        return render_template("updateDoctorAvailibility.html", 
                             availibility=availibility, 
                             doctor_user=doctor_user, 
                             doctor_details=doctor_details)
    else:
        return redirect("/login")

@updateavailibility.route("/admin/doctor/slots/update/<doctor_username>", methods=['POST'])
def updateDoctorAvailibilityByAdmin(doctor_username):
    if('user' in session and (session['role']=="admin" or (session['role']=="doctor" and session['user']==doctor_username))):
        data = request.get_json()  
        try:
            for date_str, slots in data.items():
                date_obj = datetime.date.fromisoformat(date_str)

                entry = DoctorAvailibility.query.filter_by(username=doctor_username, date=date_obj).first()

                if entry:
                    entry.time1 = slots[0]
                    entry.time2 = slots[1]
                else:
                    new_entry = DoctorAvailibility(username=doctor_username, date=date_obj, time1=slots[0], time2=slots[1])
                    db.session.add(new_entry)

            db.session.commit()
            return {"success": True}

        except Exception as e:
            print("Update error:", e)
            return {"success": False, "error": str(e)}, 500
    else:
        return {"success": False, "error": "Unauthorized"}, 401