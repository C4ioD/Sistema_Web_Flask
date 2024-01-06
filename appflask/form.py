from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from appflask.models import Usuario

class FormLogin(FlaskForm):
  email = StringField('E-mail', validators=[DataRequired(),Email()])
  senha = PasswordField('Senha', validators=[DataRequired(),Length(6,20)])
  botao_submit_login = SubmitField('Entrar')

class FormCriarConta(FlaskForm):
  username = StringField('Nome do Usuário', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired(), Email()])
  senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
  confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
  botao_submit_criarcontar = SubmitField('Criar Conta')

  def validate_email(self,email):
    usuario = Usuario.query.filter_by(email=email.data).first()
    if usuario:
      raise ValidationError('E-mail: Cadastre-se com outro e-mail ou faça login para continuar')
