from flask import Flask, render_template, redirect, request, session, flash, url_for, jsonify
from flask_app import app
from flask_app.models.game import Game
from flask_app.models.season import Season
from flask_app.models.user import User
import math



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
    seasons = Season.get_all()
    if season:
        data ={
            'season_id': season.id
        }
        games = Game.get_all_in_season(data)
        record = Game.get_record_in_season(data)
        if record['wins'] != None and record['losses'] != None:
            win_pct = round(record['wins']/(record['wins'] + record['losses']) * 100, 1) 
        else:
            win_pct = 0
            record['wins'] = 0
            record['losses'] = 0
    return render_template('schedule.html', games = games, user = user, record = record, win_pct = win_pct, seasons = seasons)



@app.route('/get_games/<int:id>', methods=['GET'])
def get_data(id):
    data ={
            'season_id': id
        }
    # jsonify will serialize data into JSON format.
    games = Game.get_all_in_season_json(data)
    record = Game.get_record_in_season(data)
    win_pct = round(record['wins']/(record['wins'] + record['losses']) * 100, 1) 
    return jsonify(games, win_pct, record)