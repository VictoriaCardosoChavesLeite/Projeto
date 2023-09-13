import json
from flask import Flask, jsonify, render_template, request, redirect, session,flash
from datetime import timedelta
from models import db, Aluno, Funcionario,Livro
from functions import cadastro_user,cadastro_book
import bcrypt
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.permanent_session_lifetime = timedelta(minutes=10)
app.secret_key = 'teste_app_1235'  # Defina sua chave secreta para as sessões
db.init_app(app)

@app.route('/')
def login():
    return render_template('pagina_login.html')

@app.route('/login', methods=['POST'])
def verificar_login():
    matricula = request.form.get('matricula')
    senha = request.form.get('password')

    if matricula and senha:
        aluno = Aluno.query.filter_by(matricula=matricula).first()
        funcionario = Funcionario.query.filter_by(matricula=matricula).first()

        if aluno and bcrypt.checkpw(senha.encode('utf-8'), aluno.senha.encode('utf-8')):
            session['matricula'] = matricula
            session['nome'] = aluno.nome
            session['tipo'] = 'aluno'
            session.permanent = True
            return redirect('/pagina_inicial_aluno')

        elif funcionario and bcrypt.checkpw(senha.encode('utf-8'), funcionario.senha.encode('utf-8')):
            session['matricula'] = matricula
            session['nome'] = funcionario.nome
            session['tipo'] = 'funcionario'
            session.permanent = True
            return redirect('/pagina_inicial_funcionario')

    return 'Credenciais inválidas'

@app.route('/pagina_inicial_aluno')
def inicial_a():
    if 'matricula' in session:
        nome = session['nome']
        return render_template('pagina_inicial_aluno.html')
    else:
        return redirect('/')

@app.route('/pagina_inicial_funcionario')
def inicial_f():
    if 'matricula' in session:
        nome = session['nome']
        return render_template('pagina_inicial_funcionario.html')
    else:
        return redirect('/')

@app.route('/pagina_cadastro')
def cadastro():
    return render_template('pagina_cadastro.html')

@app.route('/cadastro', methods=['POST'])
def add_user():
    name = request.form['nome']
    matricula = request.form['matricula']
    email = request.form['email']
    cargo = request.form['cargo']
    senha = request.form['password']

    hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    cadastro_user(name, matricula, email, hashed_password, cargo)
    return render_template('pagina_cadastro.html') 

@app.route('/pagina_cadastro_livro')
def cadastro_livro():
    return render_template('pagina_cadastro_livro.html')

@app.route('/livro', methods=['POST'])
def add_book():
    titulo = request.form['titulo']
    autor = request.form['autor']
    categoria = request.form['categoria']
    capa = request.files['picture__input']
    capa_filename = secure_filename(capa.filename)
    capa.save(f'static/image/capas/{capa_filename}')  # Salva o arquivo no sistema de arquivos
    caminho = f'static/image/capas/{capa_filename}'
    data = request.form['data']

    cadastro_book(titulo,autor,categoria,caminho,data)
    return 'Book added successfully.'

@app.route('/pagina_livros', methods=['GET', 'POST'])
def livros():
    if 'matricula' in session:
        livros = Livro.query.all()
        return render_template('pagina_livros.html', livros=livros)
    else:
        return redirect('/')

@app.route('/add_reservation', methods=['POST'])
def add_reservation():
    return None

@app.route('/logout')
def logout():
    session.pop('matricula', None)  # Remove a matrícula da sessão ao fazer logout
    return 'Logout realizado com sucesso.'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
