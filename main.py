from flask import Flask , render_template, url_for
from form import FormCriarConta, FormLogin

app = Flask(__name__)

app.config['SECRET_KEY'] = '199e6cecd95d0e59075e703f13b90924'

@app.route("/")
def login():
  form_login = FormLogin()
  form_criarconta = FormCriarConta()
  return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)



if __name__ == "__main__":
  app.run(debug=True)