from flask_babel import lazy_gettext as _
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ItemForm(FlaskForm):
    name = StringField(_('Name'), validators=[DataRequired()])
    price = DecimalField(_('Price'), validators=[DataRequired(), NumberRange(min=0, max=1000000)])
    submit = SubmitField(_('Submit'))
