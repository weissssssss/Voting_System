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
app.secret_key = 'your_secret_key'

# Initialize the database
db.init_app(app)

# Register controllers (routes) only if they exist
if auth_bp:
    app.register_blueprint(auth_bp)
if voting_bp:
    app.register_blueprint(voting_bp)

@app.route("/")   # Default home route
def home():
    return render_template("home.html")  # You can create templates/home.html later

if __name__ == "__main__":
    app.run(debug=True)
