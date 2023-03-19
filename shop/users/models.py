from datetime import datetime
from functools import wraps

from flask import abort
from flask_login import UserMixin, current_user

from shop import db, bcrypt, app


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f'Contact <{self.name}>'


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(50), unique=True, nullable=True)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, is_admin=False, phone=None):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.phone = phone
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f'{self.email}'

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def is_favorited(self, item):
        return self.favorited_items.filter_by(id=item.id).count() > 0


@app.cli.command("terminal")
def terminal():
    """
    creates two default users for testing purposes
    """
    admin = User(email='admin@admin.com', password='admin', is_admin=True)
    user = User(email='users@users.com', password='users')
    db.session.add(admin)
    db.session.add(user)
    db.session.commit()
    print(f'Created 2 users: {admin} as Admin User  and {user} as Simple User. '
          f'Passwords are "admin" and "users" respectively')


def admin_role_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return func(*args, **kwargs)

    return decorated_view
