from flask import Flask, render_template, redirect, request, Response, Blueprint, session, flash
from database import db
from models.models import Department

manageDepartments = Blueprint('manageDepartments', __name__)

@manageDepartments.route("/dashboard/admin/departments", methods=['GET', 'POST'])
def listDepartments():
    if('user' in session and session['role'] == "admin"):
        departments = Department.query.all()
        return render_template("manageDepartments.html", departments=departments)
    else:
        return redirect("/login")

@manageDepartments.route("/dashboard/admin/departments/add", methods=['GET', 'POST'])
def addDepartment():
    if('user' in session and session['role'] == "admin"):
        if request.method == "POST":
            name = request.form.get("name").strip()
            description = request.form.get("description").strip()
            
            # Check if department already exists
            existing_dept = Department.query.filter_by(name=name).first()
            if existing_dept:
                message = f"Department '{name}' already exists!"
                return render_template("invalid.html", message=message)
            
            new_department = Department(name=name, descreption=description)
            db.session.add(new_department)
            db.session.commit()
            
            return redirect("/dashboard/admin/departments")
        
        return render_template("addDepartment.html")
    else:
        return redirect("/login")

@manageDepartments.route("/dashboard/admin/departments/edit/<int:dept_id>", methods=['GET', 'POST'])
def editDepartment(dept_id):
    if('user' in session and session['role'] == "admin"):
        department = Department.query.get_or_404(dept_id)
        
        if request.method == "POST":
            name = request.form.get("name").strip()
            description = request.form.get("description").strip()
            
            # Check if another department with the same name exists
            existing_dept = Department.query.filter_by(name=name).first()
            if existing_dept and existing_dept.id != dept_id:
                message = f"Department '{name}' already exists!"
                return render_template("invalid.html", message=message)
            
            department.name = name
            department.descreption = description
            db.session.commit()
            
            return redirect("/dashboard/admin/departments")
        
        return render_template("editDepartment.html", department=department)
    else:
        return redirect("/login")

@manageDepartments.route("/dashboard/admin/departments/delete/<int:dept_id>", methods=['POST'])
def deleteDepartment(dept_id):
    if('user' in session and session['role'] == "admin"):
        # Check if any doctors are assigned to this department
        from models.models import Doctor
        doctors_in_dept = Doctor.query.filter_by(specialization=Department.query.get(dept_id).name).all()
        
        if doctors_in_dept:
            message = "Cannot delete department. There are doctors assigned to this department. Please reassign them first."
            return render_template("invalid.html", message=message)
        
        department = Department.query.get_or_404(dept_id)
        db.session.delete(department)
        db.session.commit()
        
        return redirect("/dashboard/admin/departments")
    else:
        return redirect("/login")