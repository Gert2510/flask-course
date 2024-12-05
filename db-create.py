from market import app, db
from market.models import Item, User

app.app_context().push()

db.drop_all()
db.create_all()

items = [
    {'name': 'Phone', 'barcode': '893212299897', 'price': 500, 'description': 'Samsung'},
    {'name': 'Laptop', 'barcode': '123985473165', 'price': 900, 'description': 'Apple'}
]

for item_data in items:
    item = Item(**item_data)
    db.session.add(item)

users = [
    {'username': 'gert', 'password_hash': '123456', 'email_address': 'gert@gert3000.com', 'budget': 1000},
    {'username': 'stefan', 'password_hash': '123456', 'email_address': 'stefan@gert3000.com', 'budget': 1000}
]

for user_data in users:
    user = User(**user_data)
    db.session.add(user)

db.session.commit()