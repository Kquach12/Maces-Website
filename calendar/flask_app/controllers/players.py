from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_app import app
from flask_app.models.player import Player
from flask_app.models.season import Season
from flask_app.models.user import User


@app.route('/roster')
def roster():
    user = None
    if 'user_id' in session:
        data = {
            "id": session['user_id']
        }
        user = User.get_one(data)

    # Get seasons
    seasons = Season.get_all()

    # load most recent players when page renders
    recentVar, recentJv = Player.get_season_info({'season': 5});

    #get players based on dropdown selection
    selected_season = request.args.get('season')
    data ={'season': selected_season};
    varsity, jv = Player.get_season_info(data);

    return render_template('roster.html',seasons = seasons, varsity = varsity, jv=jv, user = user, recentVar=recentVar, recentJv=recentJv)

