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
        reminders = Reminder.get_all()
        games = Game.get_all_in_season(data)
        notes = Note.get_all()

        if len(games) > 0:
            #use algo to append notes to each game without using nested loop, after sorting queries
            gameIdx = 0
            noteIdx = 0
            while noteIdx < len(notes):
                #if note's game id doesn't match game's id, move on to the next game
                if notes[noteIdx].game_id != games[gameIdx].id:
                    gameIdx += 1
                else:
                #if note's game id matches game's id, append note, and move on to the next note
                    games[gameIdx].notes.append(notes[noteIdx])
                    noteIdx += 1


    return render_template('announcements.html', games = games, reminders = reminders)

