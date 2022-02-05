from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_app import app
from flask_app.models.player import Player



@app.route('/roster')
def roster():
    players = Player.get_all()
    return render_template('roster.html', players = players)

