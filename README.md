# Agenda Virtual 📅

Este é um projeto de agenda virtual desenvolvido em Django.

## Estrutura do Projeto🏗️

- **accounts**
  - **login**: Página de login
  - **logout**: Página de logout
  - **cadastro**: Página de cadastro
  - **dashboard**: Página principal do usuário logado

- **agenda**
  - **numbers**: Página para gerenciar números de telefone
  - **email**: Página para gerenciar endereços de e-mail
  - **categoria**: Página para gerenciar categorias
  - **descricao**: Página para gerenciar descrições
  - **data_criacao**: Página para visualizar a data de criação da página do contato
  - **id**: Página para visualizar o ID do contato

- **contatos**
  - **lista**: Página para listar todos os contatos


- **media**: Armazenamento de arquivos de mídia
- **static**: Arquivos estáticos
- **templates**: Modelos HTML

## Instalação⚙️

### Windows

1. Clone o repositório: `git clone https://github.com/thaleson/Agenda-virtual`
2. Entre no diretório do projeto: `cd agenda-virtual`
3. Crie e ative um ambiente virtual: `python -m venv env` e `.\env\Scripts\activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute as migrações: `python manage.py migrate`
6. Crie um superusuário: `python manage.py createsuperuser`
7. Inicie o servidor: `python manage.py runserver`

Acesse a aplicação em [http://localhost:8000/](http://localhost:8000/) e faça login com o superusuário criado.

### Linux/Mac

1. Clone o repositório: `git clone https://github.com/thaleson/Agenda-virtual-em-django.git`
2. Entre no diretório do projeto: `cd agenda-virtual`
3. Crie e ative um ambiente virtual: `python -m venv env` e `source env/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute as migrações: `python manage.py migrate`
6. Crie um superusuário: `python manage.py createsuperuser`
7. Inicie o servidor: `python manage.py runserver`

Acesse a aplicação em [http://localhost:8000/](http://localhost:8000/) e faça login com o superusuário criado.

## Como Contribuir🤝

Se deseja contribuir para o desenvolvimento deste projeto, siga estas etapas:

1. Faça um fork do repositório
2. Crie uma branch para a sua contribuição: `git checkout -b feature/nova-feature`
3. Faça as alterações desejadas
4. Envie um pull request para a branch principal do repositório original

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
