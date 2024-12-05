from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()


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
    os.makedirs(instance_dir, exist_ok=True)

    # Application configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)

    # Set up Flask-Admin
    from dossier_app.models import Section, Reaction
    admin = Admin(app, name="Admin Panel", template_mode="bootstrap3")
    admin.add_view(ModelView(Section, db.session))
    admin.add_view(ModelView(Reaction, db.session))

    # Register blueprints
    from dossier_app.routes import main
    app.register_blueprint(main)

    return app
