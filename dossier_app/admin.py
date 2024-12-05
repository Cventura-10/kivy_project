# dossier_app/admin.py
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Adjust import to reflect relative path
from dossier_app.models import db, Section, Reaction

def setup_admin(app):
    """Sets up Flask-Admin with the application."""
    admin = Admin(app, name="Admin Panel", template_mode="bootstrap3")
    admin.add_view(ModelView(Section, db.session))  # Admin view for Section model
    admin.add_view(ModelView(Reaction, db.session))  # Admin view for Reaction model
