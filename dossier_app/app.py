from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

from dossier_app.models import db, Section, Reaction
from dossier_app.routes import main  # Import the main blueprint


def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)

    # Define the base directory dynamically
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    instance_dir = os.path.join(BASE_DIR, '..', 'instance')
    db_path = os.path.join(instance_dir, 'dossier.db')

    # Ensure the instance directory exists
    try:
        os.makedirs(instance_dir, exist_ok=True)
    except Exception as e:
        raise RuntimeError(f"Failed to create instance directory: {e}")

    # Application configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')  # Add a secret key

    # Initialize plugins
    db.init_app(app)
    migrate = Migrate(app, db)

    # Set up Flask-Admin
    try:
        admin = Admin(app, name="Admin Panel", template_mode="bootstrap3")
        admin.add_view(ModelView(Section, db.session))
        admin.add_view(ModelView(Reaction, db.session))
    except Exception as e:
        raise RuntimeError(f"Error setting up Flask-Admin: {e}")

    # Register blueprint
    try:
        app.register_blueprint(main)
    except Exception as e:
        raise RuntimeError(f"Error registering blueprint: {e}")

    return app


# Application instance
try:
    app = create_app()
except Exception as e:
    raise RuntimeError(f"Application creation failed: {e}")
