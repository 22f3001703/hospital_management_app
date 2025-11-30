from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import Doctor, User
from models.models import Department , Appointments

thepatientDashboard = Blueprint('thepatientDashboard', __name__)
@thepatientDashboard.route("/dashboard/patient", methods=['GET','POST'])
def patientDashboard():
    if('user' in session and session['role']=="patient"):
        user=session['user']
        theUser= User.query.filter_by(username=user).first()
        departments= Department.query.all()

        myappointmnets= Appointments.query.filter_by(patient=user).all()
        print("My Appointments:", myappointmnets)
        sendabledata = []
        details = {}
        for x in myappointmnets:
            getdoctorsderails=Doctor.query.filter_by(username=x.doctor).first()
            details={
                "id": x.id,
                "fullname": getdoctorsderails.fullname,
                "specialization": getdoctorsderails.specialization,
                "date": x.date,
                "timeslot": x.timeslot,
                "status": x.status
            }
            sendabledata.append(details)
        print("Sendable Data:", sendabledata)
        sendabledata.reverse()

        return render_template("patientDashboard.html",theUser=theUser,user=user, departments=departments, sendabledata=sendabledata)
    
    
    else:
        return redirect("/login")

@thepatientDashboard.route("/dashboard/patient/search", methods=['POST'])
def patientSearch():
    if('user' in session and session['role']=="patient"):
        search_type = request.form.get('search_type')
        search_query = request.form.get('search_query').strip().lower()
        
        print(f"Patient searching for: {search_query} by {search_type}")
        
        search_results = []
        
        if search_type == 'department':
            # Search doctors by department
            doctors = Doctor.query.all()
            for doctor in doctors:
                if search_query in doctor.specialization.lower():
                    # Check if doctor user is active
                    doctor_user = User.query.filter_by(username=doctor.username, role="doctor", status=1).first()
                    if doctor_user:
                        search_results.append({
                            'fullname': doctor.fullname,
                            'username': doctor.username,
                            'specialization': doctor.specialization,
                            'phone': doctor.phone
                        })
        
        elif search_type == 'doctor':
            # Search doctors by name
            doctors = Doctor.query.all()
            for doctor in doctors:
                if search_query in doctor.fullname.lower():
                    # Check if doctor user is active
                    doctor_user = User.query.filter_by(username=doctor.username, role="doctor", status=1).first()
                    if doctor_user:
                        search_results.append({
                            'fullname': doctor.fullname,
                            'username': doctor.username,
                            'specialization': doctor.specialization,
                            'phone': doctor.phone
                        })
        
        # Get regular dashboard data
        user = session['user']
        theUser = User.query.filter_by(username=user).first()
        departments = Department.query.all()
        
        myappointmnets = Appointments.query.filter_by(patient=user).all()
        sendabledata = []
        details = {}
        for x in myappointmnets:
            getdoctorsderails = Doctor.query.filter_by(username=x.doctor).first()
            details = {
                "id": x.id,
                "fullname": getdoctorsderails.fullname,
                "specialization": getdoctorsderails.specialization,
                "date": x.date,
                "timeslot": x.timeslot,
                "status": x.status
            }
            sendabledata.append(details)
        sendabledata.reverse()
        
        return render_template("patientDashboard.html",
                             theUser=theUser,
                             user=user,
                             departments=departments,
                             sendabledata=sendabledata,
                             search_results=search_results,
                             search_query=search_query,
                             search_type=search_type)
    else:
        return redirect("/login")