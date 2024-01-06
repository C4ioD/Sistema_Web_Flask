from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# Obtém o caminho do diretório atual onde está o __init__.py
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'base.db')

app.config['SECRET_KEY'] = '199e6cecd95d0e59075e703f13b90924'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

database= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from appflask import routes