from shop import db

item_user = db.Table(
    'item_user',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
)


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    favorited_users = db.relationship(
        'User', secondary=item_user, backref=db.backref('favorited_items', lazy='dynamic'), lazy='dynamic'
    )

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name}'
