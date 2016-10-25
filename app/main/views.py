from flask import render_template, session, redirect, url_for, flash
from . import main
from forms import NameForm
from ..models import User, Role


@main.route('/', methods=['GET', 'POST'])
def index():
    lista = [1, 2, 3, 4, 5]
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            print "different user"
            flash('Looks like you have changed your name!')
        user = User.query.filter_by(username=form.name.data).first()
        if user:
            flash('hahahaha')
        session['name'] = user.username
        return redirect(url_for('.index'))
    return render_template('extend.html', form=form, name=session.get('name'))
