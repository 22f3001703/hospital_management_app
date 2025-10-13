from flask import Flask,render_template,redirect,request,Response,Blueprint,session
from database import db
from models.models import User

thelogin = Blueprint('thelogin', __name__)
@thelogin.route("/login", methods=['GET','POST'])
def login():
    return render_template("login.html")