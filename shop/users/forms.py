from flask_babel import lazy_gettext as _
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    email = EmailField(_('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_('Password'), validators=[DataRequired()])
    submit = SubmitField(_('Sign in'))


class ContactForm(FlaskForm):
    email = EmailField(_('Email'), validators=[DataRequired(), Email()])
    phone = StringField(_('Phone'), validators=[DataRequired()])
    name = StringField(_('Name'), validators=[DataRequired()])
    description = StringField(_('Description'), validators=[DataRequired()], widget=TextArea())
    submit = SubmitField(_('Submit'))
