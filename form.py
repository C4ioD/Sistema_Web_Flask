from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class FormLogin(FlaskForm):
  email = StringField('E-mail')
  senha = PasswordField('Senha')
  botao_submit_login = SubmitField('Entrar')

class FormCriarConta(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
  confirmar_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
  botao_submit_criarcontar = SubmitField('Criar Conta')