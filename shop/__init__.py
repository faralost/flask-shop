import os

from dotenv import load_dotenv

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from shop.users.routes import users_bp
from shop.items.routes import items_bp

app.register_blueprint(users_bp)
app.register_blueprint(items_bp)

from shop.users.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()
