# Documentação do Código: Sistema de Biblioteca com Flask

## Visão Geral

Este código implementa um sistema de biblioteca básico utilizando o framework Flask para Python. O sistema inclui funcionalidades como login, cadastro de usuários (alunos e funcionários), cadastro de livros, exibição de livros, e logout.

## Requisitos

- Flask
- Flask-SQLAlchemy
- Flask-WTF
- bcrypt

## Estrutura de Arquivos

- `models.py`: Contém as definições das classes de modelo para o banco de dados.
- `functions.py`: Contém funções auxiliares para o cadastro de usuários e livros.

## Configuração

1. **Configuração do Flask:**
   - `SQLALCHEMY_DATABASE_URI`: Configura o URI do banco de dados (sqlite neste caso).
   - `permanent_session_lifetime`: Define a duração da sessão.
   - `secret_key`: Chave secreta para as sessões.

2. **Inicialização do Banco de Dados:**
   - O banco de dados é inicializado quando o aplicativo é executado.

## Rotas e Funcionalidades

1. **Rota `/` (login):**
   - Apresenta a página de login (`pagina_login.html`).

2. **Rota `/login` (verificar_login):**
   - Realiza a verificação das credenciais (matrícula e senha) para alunos e funcionários.
   - Inicia a sessão se as credenciais forem válidas.

3. **Rotas `/pagina_inicial_aluno` e `/pagina_inicial_funcionario`:**
   - Páginas iniciais específicas para alunos e funcionários, respectivamente.

4. **Rota `/pagina_cadastro` (cadastro):**
   - Apresenta a página de cadastro (`pagina_cadastro.html`).

5. **Rota `/cadastro` (add_user):**
   - Adiciona um usuário (aluno ou funcionário) ao banco de dados.

6. **Rota `/pagina_cadastro_livro` (cadastro_livro):**
   - Apresenta a página de cadastro de livros (`pagina_cadastro_livro.html`).

7. **Rota `/livro` (add_book):**
   - Adiciona um livro ao banco de dados, incluindo o upload da capa.

8. **Rota `/pagina_livros` (livros):**
   - Apresenta a página de exibição de livros.

9. **Rota `/add_reservation` (add_reservation):**
   - Placeholder para adicionar funcionalidade de reserva de livros.

10. **Rota `/logout`:**
   - Realiza o logout, removendo as informações da sessão.

## Execução

- O aplicativo é executado localmente usando `app.run()`.

## Observações

- A senha dos usuários é armazenada no banco de dados após ser criptografada usando bcrypt.
- As rotas `/pagina_inicial_aluno` e `/pagina_inicial_funcionario` verificam se o usuário está autenticado antes de exibir a página.

## Próximos Passos

- Implementar funcionalidades de reserva de livros.
- Adicionar validações nos formulários (por exemplo, usando Flask-WTF).
- Aprimorar a interface do usuário.
- Melhorar a segurança do sistema, como proteção contra injeção SQL.

**Nota:** Certifique-se de instalar as dependências necessárias antes de executar o código.
