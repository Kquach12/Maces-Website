from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_app import app
from flask_app.models.game import Game
from flask_app.models.season import Season



@app.route('/schedule')
def schedule():
    season = Season.get_most_recent()
    data ={
        'season_id': season.id
    }
    games = Game.get_all_in_season(data)
    return render_template('schedule.html', games = games)

