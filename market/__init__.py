from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_bcrypt import Bcrypt #Used for encrytion and decrytion of sensitive information such as passwords
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rtuncknfyhurym:fc8c21ae86a904dfe86f4025c8a8203cdda7b7f8c58cd9300bfeafe6942d16ed@ec2-44-199-22-207.compute-1.amazonaws.com:5432/d6rrssvqgqge3u'
app.config['SECRET_KEY'] = 'd1ef342105eefc1fbae07d65'
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
from market import routes