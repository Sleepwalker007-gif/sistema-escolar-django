# Sistema Escolar Django

Projeto acadêmico desenvolvido com Django para cadastro e consulta de alunos e cursos.

## Funcionalidades
- Cadastro de alunos (nome, sobrenome e e-mail).
- Cadastro de cursos (título e descrição).
- Relacionamento muitos-para-muitos: um aluno pode estar matriculado em vários cursos.
- Gerenciamento pelo Django Admin.
- Páginas públicas para visualizar alunos e cursos.

## Como executar
1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # Windows
   venv\\Scripts\\activate
   # Linux/macOS
   source venv/bin/activate
   ```
2. Instale as dependências: `pip install -r requirements.txt`
3. Crie as tabelas: `python manage.py makemigrations` e `python manage.py migrate`
4. Crie um usuário administrador: `python manage.py createsuperuser`
5. Inicie: `python manage.py runserver`

Acesse http://127.0.0.1:8000/ e o painel em http://127.0.0.1:8000/admin/.

## Tecnologias
Python, Django e SQLite.
