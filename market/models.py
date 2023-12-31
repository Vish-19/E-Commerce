from market import db
from market import bcrypt, login_manager
from flask_login import UserMixin
#Each class represents a database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    bought = db.Column(db.String(length=10000), nullable=True, default="")
    cart = db.Column(db.String(length=10000), nullable=True, default="")
    def __repr__(self):
        return f'User {self.username} - {self.id}'
    @property
    def password(self):
        return self.password
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    def check_password_correction(self, attempted_password):
            return bcrypt.check_password_hash(self.password_hash, attempted_password)

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    # real_price = db.Column(db.Integer(), nullable=False)
    # barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer())#, db.ForeignKey('user.id'))
    #seller = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f'Item {self.name}-{self.owner}'