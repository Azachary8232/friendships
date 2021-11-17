# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_user, model_friendships


@app.route('/')
def index():
    friends = model_friendships.Friendships.get_all()
    users  = model_user.User.get_all()

    return render_template('index.html', friends = friends, users = users)

@app.route('/create', methods = ['POST'])
def create():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name']
    }

    model_user.User.create(data)
    return redirect('/')