from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import db, User
from flask import session, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if username or email already exists
        existing_user = User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first()
        if existing_user:
            flash('Username or Email already taken!', 'error')
            return redirect(url_for('auth.register'))

        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('voting.index'))  # Or any other page after login
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')


@bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.')
    return redirect(url_for('auth.login'))
