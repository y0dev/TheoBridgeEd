from flask import Blueprint, request, render_template
import os
# from admin import admin_controller

# Create a Blueprint for API routes
views_bp= Blueprint('api', __name__, template_folder='views/')
# API endpoint to get a list of courses
@views_bp.route('/', methods=['GET'])
def get_landing_page():
    template_folder_path = os.path.abspath(views_bp.template_folder)
    print(os.path.exists(os.path.join(template_folder_path,'index.pug')))
    print(template_folder_path,views_bp.template_folder)
    return render_template('index.pug')