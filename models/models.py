from database import db
import datetime 

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    fullname = db.Column(db.String(50),nullable = False)
    username = db.Column(db.String(50),unique = True,nullable = False)
    password = db.Column(db.String(),nullable= False)
    role = db.Column(db.String(10),nullable=False)
    status=db.Column(db.Integer(),nullable=False,default=0)
    created_at=db.Column(db.DateTime(),default=datetime.datetime.utcnow)
    updated_at=db.Column(db.DateTime(),default=datetime.datetime.utcnow,onupdate=datetime.datetime.utcnow)

class Doctor(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    fullname = db.Column(db.String(50),nullable = False)
    username = db.Column(db.String(50),unique = True,nullable = False)
    password = db.Column(db.String(),nullable= False)
    address = db.Column(db.String(200),nullable = False)
    phone = db.Column(db.String(15),nullable = False)
    email = db.Column(db.String(50),nullable = False)
    experience = db.Column(db.String(100),nullable = False)
    specialization = db.Column(db.String(50),nullable = False)
    created_at=db.Column(db.DateTime(),default=datetime.datetime.utcnow)
    updated_at=db.Column(db.DateTime(),default=datetime.datetime.utcnow,onupdate=datetime.datetime.utcnow) 

class DoctorAvailibility(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(50),nullable = False)
    date=db.Column(db.Date(),nullable=False)
    time1=db.Column(db.Integer(),default=0)
    time2=db.Column(db.Integer(),default=0)

class Department(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(50),nullable = False)
    descreption=db.Column(db.String(200),nullable=True)

class Appointments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient = db.Column(db.String(50), nullable=False)
    doctor = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(10), nullable=False)   
    timeslot = db.Column(db.String(20), nullable=False)   
    status = db.Column(db.String(15), nullable=False)


class Treatment(db.Model):
    id =  db.Column(db.Integer(),primary_key=True)
    diagnosis=db.Column(db.String(500),nullable = False) 
    prescreption= db.Column(db.String(1000),nullable=False)
    notes=db.Column(db.String(50),nullable = False)


class Patient(db.Model):
    id=db.Column(db.Integer(),primary_key=True)   
    userid = db.Column(db.Integer(),nullable=False)
    name=db.Column(db.String(50),nullable = False)
    dob = db.Column(db.String(20),nullable = False)
    phone= db.Column(db.Integer(),nullable = False)
    email=db.Column(db.String(50),nullable = False)
    address=db.Column(db.String(200),nullable = False)
    emergencycontact=db.Column(db.String(50),nullable = False)



    
    