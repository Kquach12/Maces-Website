from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.stat import Stat
from flask_app.models.season import Season

@app.route('/stats')
def stats():
    if 'user_id' not in session:
        redirect('/')

    season = Season.get_most_recent()

    if season:
        data ={
            'season_id': season.id
        }
        players_stats = Stat.get_average_of_all_players_by_season(data)
        team_stats = Stat.get_average_of_team_by_season(data)
        seasons = Season.get_all()
    return render_template('statistics.html', players_stats = players_stats, team_stats = team_stats, seasons = seasons)



@app.route('/get_stats/<int:id>', methods=['GET'])
def get_stats(id):
    data ={
            'season_id': id
        }
    # jsonify will serialize data into JSON format.
    players_stats = Stat.get_average_of_all_players_by_season(data)
    team_stats = Stat.get_average_of_team_by_season(data)
    return jsonify(player_stats, team_stats)
