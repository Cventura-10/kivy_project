from app import db, Section  # Import your app and Section model

# Query the database for all sections
with db.session.begin():
    sections = Section.query.all()
    for section in sections:
        print(f"ID: {section.id}, Title: {section.title}")
