from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User
from models.models import Doctor
from models.models import DoctorAvailibility
import datetime

updateTheAvailibility = Blueprint('updateTheAvailibility', __name__)
@updateTheAvailibility.route("/doctor/slots/update", methods=['POST'])
def updateAvailibility():
    print("1")
    if "user" not in session:
        return {"success": False, "error": "Unauthorized"}, 401
    print("2")
    username = session["user"]
    data = request.get_json()  
    try:
        for date_str, slots in data.items():
            date_obj = datetime.date.fromisoformat(date_str)

            entry = DoctorAvailibility.query.filter_by(username=username, date=date_obj).first()

            if entry:
                entry.time1 = slots[0]
                entry.time2 = slots[1]
            else:
                new_entry = DoctorAvailibility(username=username, date=date_obj, time1=slots[0], time2=slots[1])
                db.session.add(new_entry)

        db.session.commit()
        return {"success": True}

    except Exception as e:
        print("Update error:", e)
        return {"success": False, "error": str(e)}, 500    