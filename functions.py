from models import db,Aluno,Funcionario,Livro

def get_user(matricula):
    try:
        user_a = Aluno.query.filter_by(matricula=matricula).first()
        user_f = Funcionario.query.filter_by(matricula=matricula).first()

        if user_a:
            return user_a
        if user_f:
            return user_f
    except:
        print("Algo deu errado")

def verifica(matricula,senha):
    try:
        user = get_user(matricula)
        if user.senha == senha:
            return True
        else:
            return False
    except:
        print("Algo deu errado")

def cadastro_user(name,matricula,email,senha,cargo):
    try:
        # Faça o cadastro no banco de dados aqui
        if cargo == 'aluno':
            new_user = Aluno(name, matricula, email, senha,[])
        else:
            new_user = Funcionario(name, matricula, email, senha)

        db.session.add(new_user)
        db.session.commit()

        # Se o cadastro for bem-sucedido, retorne True
        return True
    except:
        # Se ocorrer algum erro durante o cadastro, retorne False
        return False

def cadastro_book(titulo,autor,categoria,capa,data):
    new_book = Livro(titulo,autor,categoria,capa,data)

    db.session.add(new_book)
    db.session.commit()
    
    return 'Book added successfully.'