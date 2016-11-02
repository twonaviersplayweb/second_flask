from flask import render_template, session, redirect, url_for, flash
from . import main
from forms import NameForm, LoginForm, RegisterForm
from ..models import User, Role
from flask.ext.login import login_user, current_user, login_required, logout_user
from app import db, mail
from flask.ext.mail import Message


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is not None:
            flash('hahahaha')
            if current_user.is_authenticated:
                print 'haha'
            return redirect(url_for('.show'))
    return render_template('extend.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        if u is not None:
            flash("this email has been register")
            return redirect(url_for('.login'))
        user = User()
        user.email = form.email.data
        user.username = form.username.data
        db.session.add(user)
        db.session.commit()
        msg = Message("Hi!This is a test ", sender='weilezhuce12345@163.com', recipients=['playweb@163.com'])
        msg.body = 'This is a email'
        msg.html = '<b>HTML</b> body'
        mail.send(msg)
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.password_hash(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('.show'))
        flash('usr not found')
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out.')
    return redirect(url_for('.index'))


@main.route('/protect')
@login_required
def protect():
    return '<h1>Only authenticated users are allowed!</h1>'


@main.route('/show')
def show():
    return render_template('index.html')