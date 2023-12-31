from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '199e6cecd95d0e59075e703f13b90924'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'

db= SQLAlchemy(app)

from appflask import routes