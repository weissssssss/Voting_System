from flask import Flask, render_template
from models import db
from controllers import init_app

# Import blueprints safely
try:
    from controllers.auth import bp as auth_bp
    from controllers.voting import bp as voting_bp
except ImportError:
    auth_bp = None
    voting_bp = None

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Add this to suppress warning
app.secret_key = 'your_secret_key'

# Initialize the database
db.init_app(app)

with app.app_context():
    db.create_all()  # This will create the database file if it doesn't exist

# Register controllers (routes) only if they exist
if auth_bp:
    app.register_blueprint(auth_bp)
if voting_bp:
    app.register_blueprint(voting_bp)

@app.route('/testdb')
def testdb():
    try:
        db.session.execute('SELECT 1')
        return "Database connection working!"
    except Exception as e:
        return f"Database error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
