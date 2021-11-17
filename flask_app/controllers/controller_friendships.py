
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_user, model_friendships


@app.route('/create_friend', methods = ['POST'])
def create_friend():
    data = {
        'user_id' : request.form['user'],
        'friend_id' : request.form['friend']
    }

    model_friendships.Friendships.create_friendship(data)

    return redirect('/')