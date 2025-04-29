from flask_sqlalchemy import SQLAlchemy

# Create the database instance
db = SQLAlchemy()

# Import the models to register them with SQLAlchemy
from .user import User
from .vote import Vote
