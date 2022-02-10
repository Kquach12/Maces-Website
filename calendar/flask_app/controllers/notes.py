from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_app import app
from flask_app.models.note import Note



@app.route('/announcements')
def announcements():
    return render_template('announcements.html')

