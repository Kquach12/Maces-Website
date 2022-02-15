from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_app import app
from flask_app.models.note import Note
from flask_app.models.user import User



@app.route('/announcements')
def announcements():
    user = None
    if 'user_id' in session:
        data = {
            "id": session['user_id']
        }
        user = User.get_one(data)
    return render_template('announcements.html', user = user)

