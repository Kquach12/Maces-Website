from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_app import app
from flask_app.models.player import Player
from flask_app.models.user import User



@app.route('/roster')
def roster():
    user = None
    if 'user_id' in session:
        data = {
            "id": session['user_id']
        }
        user = User.get_one(data)
    varsity, jv = Player.get_season_info()
    print(varsity)
    return render_template('roster.html', varsity = varsity, jv=jv, user = user)

