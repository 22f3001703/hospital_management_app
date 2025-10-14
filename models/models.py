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