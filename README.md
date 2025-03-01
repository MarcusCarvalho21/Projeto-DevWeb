# 🐍 Smoothflow To-Do List ✅  

<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo.png" height="80">
  <img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" height="80">
</p>
**SmoothFlow** é um aplicativo de gerenciamento de tarefas desenvolvido com Django. Com uma interface intuitiva e uma dashboard dinâmica, ele permite acompanhar suas tarefas com eficiência, mantendo o foco no que realmente importa.  

## 📌 Funcionalidades  
- Adicionar, editar e excluir tarefas.  
- Marcar tarefas como concluídas.  
- Dashboard com estatísticas das tarefas.  
- Interface responsiva e fácil de usar.  

## 🚀 Como executar  

1. Clone o repositório:  
   ```sh
   git clone https://github.com/FilipeTorresBR/smoothflow.git
   cd smoothflow
   ```
2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```
3. Instale as dependências:
    ```sh
      pip install -r requirements.txt
    ```
4. Aplique as migrações:
    ```sh
      python manage.py migrate
    ```
5. Inicie o servidor:
    ```sh
      python manage.py runserver
    ```

Acesse a aplicação em http://127.0.0.1:8000/.

📷 Capturas de Tela
<p>
  <img src="https://github.com/FilipeTorresBR/smoothflow/blob/master/static/imgs/screenshots/login.png" alt="Login no site" />
  Pagina de login do site<br>
  <img src="https://github.com/FilipeTorresBR/smoothflow/blob/master/static/imgs/screenshots/lista_todo.png" alt="Lista de atividades pendentes" />
  Lista de atividades pendentes<br>
  <img src="https://github.com/FilipeTorresBR/smoothflow/blob/master/static/imgs/screenshots/nova_todo.png" alt="Adicionando uma nova atividade" />
  Adicionando uma nova atividade<br>
  <img src="https://github.com/FilipeTorresBR/smoothflow/blob/master/static/imgs/screenshots/dash.png" alt="Dashboard das atividades" />
  Dashboard das atividades<br>
</p>
  
🛠 Tecnologias Utilizadas
* Python 🐍
* Django 🏗️
* SQLite
* HTML, CSS e JavaScript para o frontend

