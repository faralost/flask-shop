import os

from dotenv import load_dotenv

from flask import Flask, request, session
from flask_babel import Babel
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_locale():
    language = session.get('language', None)
    return language if language else request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['LANGUAGES'] = ['en', 'ru']
app.config["BABEL_TRANSLATION_DIRECTORIES"] = os.path.join(BASE_DIR, '../translations')
app.config["GTAG"] = False

babel = Babel(app, locale_selector=get_locale)
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
