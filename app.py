from flask import Flask 
from database import db 
from controllers.register import registerthePatient
from controllers.login import thelogin
from controllers.patientDashboard import thepatientDashboard
from controllers.adminDashboard import theadminDashboard
from controllers.doctorDashboard import thedoctorDashboard
from controllers.registerDoctor import registertheDoctor
from controllers.provideAvailibility import provideTheAvailibility
from controllers.updateAvailibility import updateavailibility
from controllers.showDepartmentPage import showthedepartment
from controllers.provideAvailibilityToPatient import provideAvailibilityToPatient
from controllers.doctorDetails import thedoctorDetails
from controllers.bookAppointment import theAppointmentBooking
from controllers.actionToAppointment import theActionWithAppointment
from controllers.updatePatientHistory import theUpdatePatientHistory
from controllers.patientHistoryForDoctor import thePatientHistory
from controllers.logout import log_out
from controllers.editPatientDetails import theeditpatientdetails
from controllers.editDoctorDetailsByAdmin import theeditdoctordetailsbyadmin
from controllers.editPateintDetailsByAdmin import theeditpatientdetailsByAdmin
from controllers.deleteDoctor import thedeleteDoctor


def start_the_app():
    app = Flask(__name__)
    app.debug=True
    app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///hospital.db'
    db.init_app(app)
    app.app_context().push()
    app.secret_key = "123456"
    app.register_blueprint(registerthePatient)
    app.register_blueprint(thelogin)
    app.register_blueprint(thepatientDashboard)
    app.register_blueprint(theadminDashboard)
    app.register_blueprint(thedoctorDashboard)
    app.register_blueprint(registertheDoctor)
    app.register_blueprint(provideTheAvailibility)
    app.register_blueprint(updateavailibility)
    app.register_blueprint(showthedepartment)
    app.register_blueprint(provideAvailibilityToPatient)
    app.register_blueprint(thedoctorDetails)
    app.register_blueprint(theAppointmentBooking)
    app.register_blueprint(theActionWithAppointment)
    app.register_blueprint(theUpdatePatientHistory)
    app.register_blueprint(thePatientHistory)
    app.register_blueprint(log_out)
    app.register_blueprint(theeditpatientdetails)
    app.register_blueprint(theeditdoctordetailsbyadmin)
    app.register_blueprint(theeditpatientdetailsByAdmin)
    app.register_blueprint(thedeleteDoctor)
    return app

app = start_the_app()

if __name__ == "__main__":
    app.run()

