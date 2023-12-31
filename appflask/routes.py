from flask import  render_template, url_for, request, flash , redirect
from appflask import app
from appflask.form import FormCriarConta, FormLogin


@app.route('/', methods=['GET','POST'])
def home():
  return '<h1>OlaMundo<h1>'

@app.route('/criarconta', methods=['GET','POST'])
def criarconta():
  form_criarconta = FormCriarConta()
  return render_template('criarconta.html', form_criarconta=form_criarconta)


@app.route("/login", methods=['GET','POST'])
def login():
  form_login = FormLogin()
 
  if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
    flash(f'Fogin feito com sucesso no e-mail: {form_login.email.data}')
    return redirect(url_for('home'))
  
  return render_template('login.html', form_login=form_login)