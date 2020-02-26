from flask import render_template, request, redirect, flash, url_for
from app.auth.forms import LoginForm


from flask_login import current_user, login_user, logout_user
from app.models import User

from werkzeug.urls import url_parse
from app.auth import bp

@bp.route('/')
@bp.route('/login',methods=['GET','POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('Charts.charts'))

    print("you are not current user")

    lform = LoginForm()

    if lform.validate_on_submit():
        print("validate form True")
        print("username is {}".format(lform.username.data))
        print("password is {}".format(lform.password.data))
        user = User.query.filter_by(username=lform.username.data).first()
        print("requested user is,{}".format(user))
        if user is None or not user.check_password(lform.password.data):
            flash('Invalid username or password')
            print("None user or failed check password")
            return redirect(url_for('Auth.login'))
            
        print("call login_user")
        login_user(user, remember=lform.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('Charts.charts')
            print("not next page")
        return redirect(next_page)

    print("validate form False")
    return render_template('login.html', lform=lform)

@bp.route('/logout')
def logout():
    logout_user()
    print("logout")
    return redirect(url_for('Auth.login'))