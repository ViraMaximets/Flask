from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='Vanilla', password='VanillaSuper_', server='db', database='fdb')

db = SQLAlchemy(app)

engine = db.engine
Base = db.Model

@app.route('/')
def la():
    return '<h1> papayas </h1>'


if __name__ == '__main__':
    app.run()
