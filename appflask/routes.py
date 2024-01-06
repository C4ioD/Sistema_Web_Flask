from flask import  render_template, url_for, request, flash , redirect
from appflask import app, database, bcrypt
from appflask.form import FormCriarConta, FormLogin
from appflask.models import Usuario
from flask_login import login_user



@app.route('/', methods=['GET','POST'])
def home():
  return render_template('home.html')

@app.route('/criarconta', methods=['GET','POST'])
def criarconta():
  form_criarconta = FormCriarConta()
  if form_criarconta.validate_on_submit() and 'botao_submit_criarcontar' in request.form:
    senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
    usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha= senha_cript)
    database.session.add(usuario)
    database.session.commit()
    flash(f'Conta criada com sucesso!: {form_criarconta.email.data}')
    return redirect(url_for('home'))
  return render_template('criarconta.html', form_criarconta=form_criarconta)


@app.route("/login", methods=['GET','POST'])
def login():
  form_login = FormLogin()
  form_criarconta = FormCriarConta()
 
  if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
    usuario = Usuario.query.filter_by(email=form_login.email.data).first()
    if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
      login_user(usuario)
      flash(f'login feito com sucesso no e-mail: {form_login.email.data}')
      return redirect(url_for('home'))
    else:
      flash('Falha no Login! E-mail ou Senha Incorretos')
  return render_template('login.html', form_login=form_login)