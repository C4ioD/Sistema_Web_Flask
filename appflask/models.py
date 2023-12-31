from appflask import db

class Usuario(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False, unique=True)
  senha = db.Column(db.String, nullable=False)
  foto_perfil = db.Column(db.String, default='default.jpg')