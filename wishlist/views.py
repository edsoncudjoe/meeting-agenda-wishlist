from flask import render_template, redirect, url_for
from wishlist import app, db

from .forms import TopicForm
from models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TopicForm()
    if form.validate_on_submit():
        msg = form.message.data
        m = Message(title='', text=msg)
        db.session.add(m)
        db.session.commit()
        return redirect(url_for('results'))
    return render_template('index.html', form=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    form = TopicForm()
    if form.validate_on_submit():
        msg = form.message.data
        m = Message(title='', text=msg)
        db.session.add(m)
        db.session.commit()
        return redirect(url_for('results'))
    res = Message.newest(50)
    return render_template('index.html', form=form, col=res)
