from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_app import app
from flask_app.models.game import Game
from flask_app.models.season import Season
from flask_app.models.user import User



@app.route('/schedule')
def schedule():
    user = None
    games = None
    if 'user_id' in session:
        data = {
            "id": session['user_id']
        }
        user = User.get_one(data)
    season = Season.get_most_recent()
    if season:
        data ={
            'season_id': season.id
        }
        games = Game.get_all_in_season(data)
    return render_template('schedule.html', games = games, user = user)

