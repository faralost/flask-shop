from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

from shop import app
from shop.forms import LoginForm
from shop.models import Item, User


@app.route('/')
def index():
    items = Item.query.all()
    return render_template('shop/index.html', items=items)


@app.route('/items/<int:pk>')
def item_detail(pk):
    item = Item.query.get_or_404(pk)
    return render_template('shop/item.html', item=item)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in', 'info')
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'danger')
            return render_template('user/login.html', form=form)
    return render_template('user/login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You were logged out', 'success')
    return redirect(url_for('index'))
