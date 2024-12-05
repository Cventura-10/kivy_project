import os
from app import app, db, Section

CONTENT_DIR = "/Users/carlosventura/kivy_project/dossier_app/dossier_content"

def load_content():
    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith(".txt"):
            title = filename.replace("_", " ").replace(".txt", "").capitalize()
            with open(os.path.join(CONTENT_DIR, filename), 'r') as file:
                content = file.read()
            section = Section(title=title, content=content)
            db.session.add(section)
    db.session.commit()
    print("Content loaded into the database.")

if __name__ == "__main__":
    with app.app_context():  # Set up application context
        db.create_all()  # Create all tables
        load_content()  # Populate database with content
