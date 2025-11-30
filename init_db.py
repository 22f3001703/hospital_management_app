from app import start_the_app
from database import db
from models.models import User

app = start_the_app()

with app.app_context():
    db.create_all()
    print("Database and tables created ✅")
    print("creating admin ☑️")
    admin = User(
        fullname="Aashish Jha",
        username="jhaempire",
        password="error",
        role="admin",
        status=1
    )
    db.session.add(admin)
    db.session.commit()

    print("The admin is created succesfully🍀")
    