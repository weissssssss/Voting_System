# setup_db.py

from app import app
from models import db
from models.vote import Candidate

# Define initial candidate names
candidate_names = ["Candidate A", "Candidate B", "Candidate C"]

with app.app_context():
    # Create tables
    db.create_all()

    # Seed candidates if not already present
    if Candidate.query.count() == 0:
        print("Seeding candidates...")
        candidates = [Candidate(name=name) for name in candidate_names]
        db.session.add_all(candidates)
        db.session.commit()
        print("Candidates added successfully.")
    else:
        print("Candidates already exist. Skipping seeding.")
