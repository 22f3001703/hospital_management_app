from flask import Flask 
from database import db 
from controllers.register import registerthePatient
from controllers.login import thelogin


def start_the_app():
    app = Flask(__name__)
    app.debug=True
    app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///hospital.db'
    db.init_app(app)
    app.app_context().push()
    app.secret_key = "123456"
    app.register_blueprint(registerthePatient)
    app.register_blueprint(thelogin)
    return app

app = start_the_app()

if __name__ == "__main__":
    app.run()

