import json
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Funcionario(db.Model):
    matricula = db.Column(db.String(10), primary_key=True)
    nome = db.Column(db.String(300))
    email = db.Column(db.String(200))
    senha = db.Column(db.String(300))

    def __init__(self, nome, matricula, email, senha):
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.senha = senha


class Aluno(db.Model):
    matricula = db.Column(db.String(10), primary_key=True)
    nome = db.Column(db.String(300))
    email = db.Column(db.String(200))
    senha = db.Column(db.String(300))
    reservas = db.Column(db.String(500))

    def __init__(self, nome, matricula, email, senha, reservas):
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.senha = senha
        self.reservas = json.dumps(reservas) if reservas else '[]'

    def add_reservation(self, book_title):
        reservas_list = json.loads(self.reservas)
        if len(reservas_list) < 5:
            if book_title and book_title not in reservas_list:
                reservas_list.append(book_title)
                self.reservas = json.dumps(reservas_list)
                db.session.commit()
                return True
        return False

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(300))
    autor = db.Column(db.String(200))
    categoria = db.Column(db.String(300))
    capa = db.Column(db.String(300))
    data = db.Column(db.String(300))
    estoque = db.Column(db.String(300))

    def __init__(self,titulo,autor,categoria,capa,data,estoque=0):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.capa = capa
        self.data = data
        self.estoque = estoque