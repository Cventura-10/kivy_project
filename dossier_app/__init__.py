"""
Initialization module for dossier_app.
"""
from dossier_app.app_factory import create_app, db

__all__ = ["create_app", "db"]

from dossier_app import create_app, db
from dossier_app.models import Section
from dossier_app.app_factory import create_app, db

__all__ = ["create_app", "db"]

app = create_app()

with app.app_context():
    # Reset and recreate tables (use caution with drop_all in production)
    db.drop_all()
    db.create_all()

    # Populate sections
    sections = [
        Section(
            name="Portada",
            description="Candidatura a la Presidencia de la Cámara de Cuentas - Carlos Ventura",
            image_path="images/logo.png"
        ),
        Section(
            name="Resumen Ejecutivo",
            description=(
                "Experiencia: Más de 15 años liderando procesos de control interno.\n"
                "Logros: Redacción del anteproyecto para la reforma de la Ley 10-08.\n"
                "Visión: Transformar la Cámara de Cuentas en un modelo de transparencia."
            ),
            audio_path="audio/1.mp3"
        ),
        Section(
            name="Propuestas de Mejora",
            description=(
                "1. Adopción de tecnologías avanzadas.\n"
                "2. Capacitación del personal.\n"
                "3. Optimización de procesos.\n"
                "4. Transparencia y participación ciudadana.\n"
                "5. Colaboración internacional."
            ),
            audio_path="audio/4.mp3"
        )
    ]

    # Add sections to the database
    db.session.add_all(sections)
    db.session.commit()

    print("Database seeded successfully!")
