from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from flask_app.models.game import Game
from flask_app.models.season import Season
from flask_app.models.eligible_email import Eligible_email

bcrypt = Bcrypt(app)

@app.route('/login')
def login_page():
    user = None
    if 'user_id' in session:
        data = {
            "id": session['user_id']
        }
        user = User.get_one(data)
    return render_template('login.html', user = user)

@app.route('/register', methods = ["POST"])
def register_user():
    if not User.validate_email(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "is_admin": request.form['is_admin'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    if not User.validate_login(request.form):
        # we redirect to the template with the form.
        return redirect('/login')
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        return redirect('/login')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/")


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/')
def home():
    user = None
    if 'user_id' in session:
        data = {
            "id": session['user_id']
        }
        user = User.get_one(data)
    games = Game.get_upcoming_in_season()
    return render_template("home.html", games = games, user = user)

@app.route('/admin')
def admin_page():
    if 'user_id' not in session:
        redirect('/')
    user = User.get_one({"id": session['user_id']})
    if user.is_admin != 1:
        redirect('/')

    eligible_emails = Eligible_email.get_all()

    seasons = Season.get_all()

    return render_template("admin.html", seasons=seasons)

@app.route('/new/season', methods=['POST'])
def new_season():
    data = {
        'start_year':request.form['start_year'],
        'end_year': request.form['end_year']
    }
    Season.save(data)
    return redirect('/admin')

