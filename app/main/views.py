from flask import render_template, session, redirect, url_for, flash
from . import main
from forms import NameForm
from ..models import User, Role
from flask.ext.login import login_user, current_user, login_required


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is not None:
            flash('hahahaha')
            login_user(user)
            session['name'] = user.username
            return redirect(url_for('.index'))
    print current_user
    return render_template('extend.html', form=form, name=session.get('name'))


@main.route('/protect')
@login_required
def protect():
    return '<h1>Only authenticated users are allowed!'
