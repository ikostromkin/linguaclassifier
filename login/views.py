from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from .forms import LoginForm
from models import *
from hashlib import md5

login_blueprint = Blueprint('login', __name__)


@login_blueprint.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = Users.get(email=form.email.data)
            if user:
                if user.is_activate:
                    test = form.password.data.encode('utf-8')
                    if md5(test).hexdigest() == user.password:
                        login_user(user)
                        return redirect(url_for('index'))
                    else:
                        flash('Неверный email или пароль')
                        return redirect(url_for('login.login'))
                else:
                    flash('To verify the data provided we have sent you a confirmation email')
                    return redirect(url_for('login.login'))
        except DoesNotExist:
            flash('Неверный email или пароль')
            return redirect(url_for('login.login'))

    return render_template('login.html', form=form)


@login_blueprint.route('/join/')
def join():
    return redirect(url_for('index'))


@login_blueprint.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))
