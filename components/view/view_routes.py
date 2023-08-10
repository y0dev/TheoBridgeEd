from flask import Blueprint, request, jsonify
# from admin import admin_controller

# Create a Blueprint for API routes
views_blueprint = Blueprint('api', __name__)

# API endpoint to get a list of courses
@views_blueprint.route('/', methods=['GET'])
def get_landing_page():
    courses_data = [{'id': 1, 'title': 'sample'}]
    return jsonify(courses_data)