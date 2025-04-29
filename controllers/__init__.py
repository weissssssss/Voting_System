from .auth import bp as auth_bp
from .voting import bp as voting_bp

# Make sure to register the blueprints
def init_app(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(voting_bp)
