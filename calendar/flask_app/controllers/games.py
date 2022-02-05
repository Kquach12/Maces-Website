from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_app import app



@app.route('/schedule')
def schedule():

    return render_template('schedule.html')

