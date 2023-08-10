from datetime import datetime
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myapp_db"
mongo = PyMongo(app)

class Course:
    def __init__(self, title, description, enrollment_limit):
        self.title = title
        self.description = description
        self.enrollment_limit = enrollment_limit
        self.enrolled_students = []

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "enrollment_limit": self.enrollment_limit,
            "enrolled_students": self.enrolled_students
        }
    
class Student:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}