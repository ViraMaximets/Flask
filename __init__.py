from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='Vanilla', password='VanillaSuper_', server='localhost', database='fdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'thisisthesecretkey'
app.config['JWT_ALGORITHM'] = 'HS256'

db = SQLAlchemy(app)
engine = db.engine
Base = db.Model
