from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Vanilla:VanillaSuper_@db/flask'
db = SQLAlchemy(app)




@app.route('/')
def la():
    return '<h1> papayas </h1>'

if __name__ == '__main__':
    app.run()
