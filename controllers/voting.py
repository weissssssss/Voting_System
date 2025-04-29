from flask import Blueprint, render_template, request, redirect, url_for
from models.vote import Vote
from models.user import User
from models import db

bp = Blueprint('voting', __name__)

# Sample voting options
options = ['Candidate A', 'Candidate B', 'Candidate C']

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/vote', methods=['GET'])
def show_vote_page():
    return render_template('vote.html', options=options)

@bp.route('/vote/<option>', methods=['POST'])
def vote(option):
    # Get the user (this is just a placeholder; replace with proper auth)
    user = User.query.first()
    if user:
        vote = Vote(user_id=user.id, option=option)
        db.session.add(vote)
        db.session.commit()
        return redirect(url_for('voting.results'))
    return redirect(url_for('voting.index'))

@bp.route('/results')
def results():
    vote_counts = {option: Vote.query.filter_by(option=option).count() for option in options}
    return render_template('results.html', vote_counts=vote_counts)
