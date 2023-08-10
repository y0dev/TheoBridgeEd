from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configuration for MongoDB
from config.app_config import AppConfig
from config.database_config import DatabaseConfig
app.config["MONGO_URI"] = DatabaseConfig.MONGO_URI
mongo = PyMongo(app)

# Register the API blueprint
from components.view.view_routes import views_bp
app.register_blueprint(views_bp, url_prefix='/')

# from components.courses.course_routes import course_blueprint
# app.register_blueprint(course_blueprint, url_prefix='/api/v1')



if __name__ == '__main__':
    app.run(debug=AppConfig.DEBUG)