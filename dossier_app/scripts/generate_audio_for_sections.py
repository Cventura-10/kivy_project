from app import app, db, Section
from utils import generate_audio
import os
import logging

AUDIO_DIR = os.path.join("static", "audio")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_audio_to_sections():
    # Ensure the audio directory exists
    try:
        if not os.path.exists(AUDIO_DIR):
            os.makedirs(AUDIO_DIR)
            logger.info(f"Created directory: {AUDIO_DIR}")
    except Exception as e:
        logger.error(f"Failed to create directory {AUDIO_DIR}: {e}")
        return

    # Query all sections from the database
    try:
        sections = Section.query.all()
        logger.info(f"Found {len(sections)} sections.")
    except Exception as e:
        logger.error(f"Failed to query sections: {e}")
        return

    # Generate audio for each section
    for section in sections:
        try:
            filename = os.path.join(AUDIO_DIR, f"{section.id}.mp3")
            generate_audio(section.content, filename)
            section.audio_path = os.path.join("audio", f"{section.id}.mp3")  # Store relative path
            logger.info(f"Generated audio for section {section.id}: {filename}")
        except Exception as e:
            logger.error(f"Failed to generate audio for section {section.id}: {e}")
            continue

    # Commit changes to the database
    try:
        db.session.commit()
        logger.info("Audio paths updated in the database.")
    except Exception as e:
        logger.error(f"Failed to commit changes to the database: {e}")

if __name__ == "__main__":
    with app.app_context():
        add_audio_to_sections()
