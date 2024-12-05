from dossier_app import create_app, db
from dossier_app.models import Section

app = create_app()

with app.app_context():
    sections = Section.query.all()
    for section in sections:
        print(f"ID: {section.id}, Name: {section.name}, Description: {section.description}")
