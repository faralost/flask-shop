from flask import render_template

from shop import app
from shop.models import Item


@app.route('/')
def index():
    items = Item.query.all()
    return render_template('shop/index.html', items=items)


@app.route('/items/<int:pk>')
def item_detail(pk):
    item = Item.query.get_or_404(pk)
    return render_template('shop/item.html', item=item)
