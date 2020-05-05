"""
all the stuff related to authentication is done here.
Like, login, register, configure flask_login plugin, etc.
"""
from flask import (
    Blueprint, flash, g, request, redirect, render_template, url_for, views, session
)
from app import login_manager, db
import flask_login
from .models import User

bp = Blueprint('auth',__name__)


login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please login to visit this page!'
login_manager.login_message_category = 'warning'


@login_manager.user_loader
def user_loader(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is None:
        return None
    user_id = int(user_id)
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.','warning')
    return redirect(url_for('auth.login'))

@bp.route('/logout')
def logout(): # logout a user
    flask_login.logout_user()
    session.clear()
    return redirect(url_for('index'))

class LoginView(views.MethodView): # login a user
    def get(self):
        return render_template('login.html')
    def post(self):
        """Log in a registered user by adding the user id to the session."""
        username = request.form["username"]
        password = request.form["password"]
        error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = "Incorrect username."
        elif not user.check_password(password):
            error = "Incorrect password."

        if error is None:
            # store the user id in a new session and return to the index
            flask_login.login_user(user)
            return redirect(url_for("index"))

        flash(error,'error')
        return redirect(url_for('auth.login'))

bp.add_url_rule('/login',view_func=LoginView.as_view('login'))

class RegisterView(views.MethodView):
    def get(self):
        return render_template('register.html')
    def post(self): # register a user
        username = request.form["username"]
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif db.session.query(
            User.query.filter_by(username=username).exists()
        ).scalar():
            error = f"User {username} is already registered."

        if error is None:
            # the name is available, create the user and go to the login page
            db.session.add(User(username=username, password=password))
            db.session.commit()
            return redirect(url_for("auth.login"))

        flash(error)
        return redirect(url_for('auth.register'))
        
bp.add_url_rule('/register',view_func=RegisterView.as_view('register'))


