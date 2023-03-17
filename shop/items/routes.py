from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required

from shop import db
from shop.items.forms import ItemForm
from shop.items.models import Item
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
