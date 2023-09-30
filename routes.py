from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
import random
from datetime import datetime

from models import Task
import forms
from random_words_generator import initialiseGrid, shuffleKeys, shuffleValues

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, compliment='Better Than You')

@app.route('/nora', methods=['GET', 'POST'])
def nora():
    number = 0
    form = forms.AddNumberForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        try:
            number = int(form.title.data)*2
        except:
            number = str(form.title.data) + ' * 2'
        flash('Jeff Bezos keeps your numbers safe')
        #return redirect(url_for('index'))
    return render_template('nora.html', number=number, form=form)


@app.route('/bulgarians', methods=['GET'])
def bulgarians():
    global grid
    grid = initialiseGrid()
    keys = shuffleKeys(grid)
    values = shuffleValues(grid)
    return render_template('match.html',keys=keys, values=values)