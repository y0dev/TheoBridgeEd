from flask import Blueprint, request, jsonify
# from admin import admin_controller

# Create a Blueprint for API routes
course_blueprint = Blueprint('api', __name__)

# API endpoint to get a list of courses
@course_blueprint.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()  # Fetch courses from the database
    courses_data = [{'id': course.id, 'title': course.title} for course in courses]
    return jsonify(courses_data)