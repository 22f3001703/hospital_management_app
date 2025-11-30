#!/usr/bin/env python3
"""
Test script to verify department management functionality
"""
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from database import db
from models.models import Department

def test_departments():
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Check if departments already exist
        existing_depts = Department.query.all()
        print(f"Existing departments: {len(existing_depts)}")
        
        if len(existing_depts) == 0:
            # Add some sample departments
            sample_departments = [
                {
                    "name": "Cardiology",
                    "description": "Heart and cardiovascular system specialists providing comprehensive cardiac care including diagnosis and treatment of heart diseases."
                },
                {
                    "name": "Neurology",
                    "description": "Brain and nervous system specialists treating disorders of the brain, spinal cord, and peripheral nervous system."
                },
                {
                    "name": "Orthopedics",
                    "description": "Bone, joint, and muscle specialists providing surgical and non-surgical treatment for musculoskeletal conditions."
                },
                {
                    "name": "Pediatrics",
                    "description": "Specialized medical care for infants, children, and adolescents up to 18 years of age."
                },
                {
                    "name": "Dermatology",
                    "description": "Skin, hair, and nail specialists providing medical and cosmetic treatments for various skin conditions."
                }
            ]
            
            for dept_data in sample_departments:
                dept = Department(name=dept_data["name"], descreption=dept_data["description"])
                db.session.add(dept)
            
            db.session.commit()
            print("Sample departments added successfully!")
        
        # List all departments
        all_departments = Department.query.all()
        print("\nAll Departments:")
        for dept in all_departments:
            print(f"- ID: {dept.id}, Name: {dept.name}")
            print(f"  Description: {dept.descreption}")
            print()

if __name__ == "__main__":
    test_departments()