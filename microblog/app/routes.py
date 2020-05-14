from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

user = {'username' : 'user_name_here'}
@app.route('/')
@app.route('/index')
def index():
    posts = [
        {'author':{'username': 'John'}, 'body':'Bill Gates comunista S2'},
        {'author':{'username': 'Susan'}, 'body':'Babu devia ter ganho o BBB20'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        user['username'] = form.username.data
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
