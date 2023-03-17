from flask import Blueprint, render_template

from shop.items.models import Item

items_bp = Blueprint('items', __name__)


@items_bp.route('/')
def index():
    items = Item.query.all()
    return render_template('items/index.html', items=items)


@items_bp.route('/items/<int:pk>')
def item_detail(pk):
    item = Item.query.get_or_404(pk)
    return render_template('items/item.html', item=item)
