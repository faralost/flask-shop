from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import current_user, login_user, login_required, logout_user

from shop import db
from shop.users.forms import LoginForm, ContactForm
from shop.users.models import User, Contact

users_bp = Blueprint('users', __name__)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in', 'info')
        return redirect(url_for('items.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            return redirect(url_for('items.index'))
        else:
            flash('Invalid email or password', 'danger')
            return render_template('users/login.html', form=form)
    return render_template('users/login.html', form=form)


@users_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You were logged out', 'success')
    return redirect(url_for('users.login'))


@users_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            email=form.email.data, phone=form.phone.data, name=form.name.data, description=form.description.data
        )
        db.session.add(contact)
        db.session.commit()
        flash(f'Thank you! We will contact you soon..', 'success')
        return redirect(url_for('items.index'))
    if not current_user.is_anonymous:
        form.email.data = current_user.email
        form.phone.data = current_user.phone
    return render_template('users/contact.html', form=form)
