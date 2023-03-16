from flask import render_template

from shop import app
from shop.models import Item


@app.route('/')
def index():
    items = Item.query.all()
    return render_template('shop/index.html', items=items)