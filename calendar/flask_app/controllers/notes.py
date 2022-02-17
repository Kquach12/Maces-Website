from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_app import app
from flask_app.models.note import Note
from flask_app.models.user import User
from flask_app.models.season import Season
from flask_app.models.game import Game
from flask_app.models.reminder import Reminder



@app.route('/announcements')
def announcements():
    user = None
    notes = None
    season = Season.get_most_recent()
    if 'user_id' not in session:
        redirect('/')

    if season:
        data ={
            'season_id': season.id
        }
        games = Game.get_all_in_season(data)
        reminders = Reminder.get_all()
        # notes = Note.get_all_in_season_with_games(data)
        notes = Note.get_all()
        print(games)
        print(len(notes))

        #use algo to append notes to each game without using nested loop, after sorting queries
        gameIdx = 0
        noteIdx = 0
        while noteIdx < len(notes):
            if notes[noteIdx].game_id != games[gameIdx].id:
                gameIdx += 1
            else:
                games[gameIdx].notes.append(notes[noteIdx])
                noteIdx += 1


    return render_template('announcements.html', games = games, reminders = reminders)

