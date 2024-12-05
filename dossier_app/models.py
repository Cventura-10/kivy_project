from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Section(db.Model):
    """Model representing a section in the dossier."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    views = db.Column(db.Integer, default=0)
    audio_path = db.Column(db.String(200), nullable=True)
    image_path = db.Column(db.String(200), nullable=True)


class Reaction(db.Model):
    """Model representing reactions to a section."""
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    reaction_type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(100), nullable=True)

    section = db.relationship('Section', backref=db.backref('reactions', lazy='dynamic'))
