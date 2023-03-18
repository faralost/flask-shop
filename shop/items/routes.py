from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from flask_login import login_required

from shop import db
from shop.items.forms import ItemForm
from shop.items.models import Item
from shop.items.utils import get_cart_total_price
from shop.users.models import admin_role_required

items_bp = Blueprint('items', __name__)


@items_bp.route('/')
def index():
    items = Item.query.order_by(Item.id.desc()).all()
    return render_template('items/index.html', items=items)


@items_bp.route('/items/<int:pk>')
def item_detail(pk):
    item = Item.query.get_or_404(pk)
    return render_template('items/item.html', item=item)


@items_bp.route('/items/create', methods=['GET', 'POST'])
@login_required
@admin_role_required
def item_create():
    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data, price=form.price.data)
        db.session.add(item)
        db.session.commit()
        flash(f'Successfully created new item: {item}', 'success')
        return redirect(url_for('items.index'))
    return render_template('items/create.html', form=form)


@items_bp.route('/items/<int:pk>/update', methods=['GET', 'POST'])
@login_required
@admin_role_required
def item_update(pk):
    item = Item.query.get_or_404(pk)
    form = ItemForm()
    if form.validate_on_submit():
        item.name = form.name.data
        item.price = form.price.data
        db.session.add(item)
        db.session.commit()
        flash(f'Successfully updated item: {item}', 'success')
        return redirect(url_for('items.item_detail', pk=item.id))
    form.name.data = item.name
    form.price.data = item.price
    return render_template('items/update.html', form=form, item=item)


@items_bp.route('/items/<int:pk>/delete')
@login_required
@admin_role_required
def item_delete(pk):
    item = Item.query.get_or_404(pk)
    db.session.delete(item)
    db.session.commit()
    flash(f'Item {item} was deleted', 'danger')
    return redirect(url_for('items.index'))


@items_bp.route('/items/<int:pk>/add_to_cart', methods=['POST'])
def add_to_cart(pk):
    item = Item.query.get_or_404(pk)
    dict_items = {str(pk): {'name': item.name, 'price': str(item.price), 'quantity': 1}}
    if 'cart' in session:
        if str(pk) in session['cart']:
            flash(f'{item} already in cart', 'warning')
        else:
            session['cart'] = session['cart'] | dict_items
    else:
        session['cart'] = dict_items
        session.modified = True
    return redirect(request.form.get('next'))


@items_bp.route('/cart')
def cart():
    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('items.index'))
    total = get_cart_total_price(session['cart'])
    return render_template('items/cart.html', total=total)


@items_bp.route('/clear-cart')
def clear_cart():
    session.pop('cart', None)
    flash('Your cart is empty', 'warning')
    return redirect(url_for('items.index'))


@items_bp.route('/cart/items/<int:pk>/update', methods=['POST'])
def update_cart_item(pk):
    if 'cart' not in session:
        return redirect(url_for('items.index'))
    quantity = request.form.get('quantity') or 1
    for item_id, item in session['cart'].items():
        if int(item_id) == pk:
            item['quantity'] = quantity
            flash(f'{item["name"]} quantity in cart was updated', 'success')
    return redirect(url_for('items.cart'))


@items_bp.route('/cart/items/<int:pk>/delete')
def delete_cart_item(pk):
    session.modified = True
    for item_id, item in list(session['cart'].items()):
        if int(item_id) == pk:
            session['cart'].pop(item_id, None)
    return redirect(url_for('items.cart'))
