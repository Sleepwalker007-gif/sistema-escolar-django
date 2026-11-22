# Sistema de Gestão Escolar

Projeto acadêmico desenvolvido com Django para gerenciar alunos e cursos.

## Requisitos
- Python 3.10 ou superior
- pip

## Funcionalidades
- Cadastro de alunos: nome, sobrenome e e-mail.
- Cadastro de cursos: título e descrição.
- Relacionamento muitos-para-muitos: cada aluno pode estar matriculado em vários cursos e cada curso pode ter vários alunos.
- Administração dos registros pelo Django Admin.
- Páginas públicas para listar alunos e cursos.

## Instalação no Windows (VS Code)
Abra a pasta do projeto no VS Code e, no terminal, execute:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py makemigrations escola
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Se o PowerShell bloquear a ativação do ambiente, execute temporariamente:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

No navegador:
- Página inicial: http://127.0.0.1:8000/
- Alunos: http://127.0.0.1:8000/alunos/
- Cursos: http://127.0.0.1:8000/cursos/
- Administração: http://127.0.0.1:8000/admin/

## Como testar
1. Entre em `/admin/` com o usuário criado.
2. Cadastre pelo menos dois cursos.
3. Cadastre um aluno e selecione um ou mais cursos no campo de matrícula.
4. Abra `/alunos/` e `/cursos/` para conferir as listagens e os relacionamentos.

## Estrutura
```text
sistema_escolar_django/
├── manage.py
├── requirements.txt
├── README.md
├── sistema_escolar/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── escola/
    ├── models.py
    ├── admin.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    └── templates/escola/
```

## Observação acadêmica
Antes da entrega, execute os comandos de instalação e teste as páginas no seu computador. O banco SQLite local não é enviado, pois será criado automaticamente com `migrate`.
