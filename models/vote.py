from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    option = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<Vote {self.option}>'
