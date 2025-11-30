from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User, Patient
from models.models import Doctor , Appointments

theadminDashboard = Blueprint('theadminDashboard', __name__)
@theadminDashboard.route("/dashboard/admin", methods=['GET','POST'])
def adminDashboard():
    if('user' in session and session['role']=="admin"):
        user=session['user']
        print(user)
        alldoctors=User.query.filter_by(role="doctor",status=1).all()
        print(alldoctors)
        doctdetails= Doctor.query.all()
        print(doctdetails)
        allpatients=User.query.filter_by(role="patient",status=1).all()
        print(allpatients)
        patientdetails= Patient.query.all()
        print(patientdetails)
        for x in patientdetails:
            print(x.email)
        allappointment= Appointments.query.all()
        print(allappointment)
        allappointments=[]
        added_usernames = set()
        innerdetails={}
        for appointment in allappointment:
            patient=User.query.filter_by(username=appointment.patient).first()
            doctor=User.query.filter_by(username=appointment.doctor).first()
            department = Doctor.query.filter_by(username=appointment.doctor).first().specialization
            if(appointment.patient not in added_usernames):
                innerdetails={
                    'id':appointment.id,      
                    'patient_fullname':patient.fullname,
                    'doctor_fullname':doctor.fullname,
                    'department':department,    
                    'date':appointment.date,
                    'timeslot':appointment.timeslot,
                    'status':appointment.status,
                    'pt_username':appointment.patient,
                }
                added_usernames.add(appointment.patient)
                allappointments.append(innerdetails)

        
        return render_template("adminDashboard.html",user=user , alldoctors=alldoctors, doctdetails=doctdetails, allpatients=allpatients, patientdetails=patientdetails , allappointments=allappointments)
    else:
        return redirect("/login")

@theadminDashboard.route("/dashboard/admin/search", methods=['POST'])
def adminSearch():
    if('user' in session and session['role']=="admin"):
        search_type = request.form.get('search_type')
        search_query = request.form.get('search_query').strip().lower()
        
        print(f"Searching for: {search_query} in {search_type}")
        
        search_results = []
        
        if search_type == 'doctor':

            doctors = User.query.filter_by(role="doctor", status=1).all()
            for doctor in doctors:
                if (search_query in doctor.fullname.lower() or 
                    search_query in doctor.username.lower()):
                    doctor_details = Doctor.query.filter_by(username=doctor.username).first()
                    if doctor_details:
                        search_results.append({
                            'user': doctor,
                            'doctor_details': doctor_details
                        })
        
        elif search_type == 'patient':

            patients = User.query.filter_by(role="patient", status=1).all()
            for patient in patients:
                if (search_query in patient.fullname.lower() or 
                    search_query in patient.username.lower()):
                    patient_details = Patient.query.filter_by(userid=patient.id).first()
                    if patient_details:
                        search_results.append({
                            'user': patient,
                            'patient_details': patient_details
                        })

        user = session['user']
        alldoctors = User.query.filter_by(role="doctor", status=1).all()
        doctdetails = Doctor.query.all()
        allpatients = User.query.filter_by(role="patient", status=1).all()
        patientdetails = Patient.query.all()
        

        allappointment = Appointments.query.all()
        allappointments = []
        for appointment in allappointment:
            patient = User.query.filter_by(username=appointment.patient).first()
            doctor = User.query.filter_by(username=appointment.doctor).first()
            department = Doctor.query.filter_by(username=appointment.doctor).first().specialization
            if(appointment.status == "booked"):
                innerdetails = {
                    'id': appointment.id,      
                    'patient_fullname': patient.fullname,
                    'doctor_fullname': doctor.fullname,
                    'department': department,    
                    'date': appointment.date,
                    'timeslot': appointment.timeslot,
                    'status': appointment.status,
                    'pt_username': appointment.patient,
                }
                allappointments.append(innerdetails)
        
        return render_template("adminDashboard.html", 
                             user=user, 
                             alldoctors=alldoctors, 
                             doctdetails=doctdetails, 
                             allpatients=allpatients, 
                             patientdetails=patientdetails, 
                             allappointments=allappointments,
                             search_results=search_results,
                             search_query=search_query,
                             search_type=search_type)
    else:
        return redirect("/login")