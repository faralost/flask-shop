# Проект простого онлайн магазина  

Выполнен в качестве тестового задания

# Стек
<li>Python
<li>Flask
<li>Postgres
<li>Docker


# Установка и запуск
1. Склонируйте репозиторий

2. Перейдя в директорию с проектом создайте файл .env и заполните по примеру:

```
FLASK_APP=run.py
FLASK_DEBUG=true
FLASK_RUN_PORT=8000
SQLALCHEMY_DATABASE_URI=postgresql://postgres:postgres@db:5432/postgres
SECRET_KEY=secret_here

POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
POSTGRES_HOST=db
DATABASE=postgres
```

3. Чтобы запустить проект выполните:

```
docker compose up --build -d
```

4. Затем для создания двух базовых юзеров выполните:
```
docker exec -it flaskproject-app-1 flask terminal
```
<li>admin@admin.com - с паролем 'admin'
<li>user@user.com - с паролем 'user'
