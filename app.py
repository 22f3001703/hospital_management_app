from flask import Flask 
from database import db 


def start_the_app():
    app = Flask(__name__)
    app.debug=True
    app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///hospital.db'
    db.init_app(app)
    app.app_context().push()
    app.secret_key = "123456"
    return app

app = start_the_app()

if __name__ == "__main__":
    app.run()

