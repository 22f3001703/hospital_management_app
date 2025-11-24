from flask import Flask,redirect,Blueprint,session


log_out = Blueprint('logout', __name__)
@log_out.route("/logout", methods=['GET','POST'])
def logout():
    session.clear()
    return redirect("/login")