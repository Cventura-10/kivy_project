from dossier_app.app import app
from flask_migrate import Migrate
from dossier_app.models import db  # Make sure this is the SQLAlchemy instance

# Initialize Flask-Migrate
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()
