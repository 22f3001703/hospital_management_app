from database import db
import datetime 

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    fullname = db.Column(db.String(50),nullable = False)
    username = db.Column(db.String(50),unique = True,nullable = False)
    password = db.Column(db.String(),nullable= False)
    role = db.Column(db.String(10),nullable=False)
    status=db.Column(db.Integer(),nullable=False,default=0)