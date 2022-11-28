# Тестовое задание, компания DFA Media

### Технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/) [![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/) [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/) [![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/) [![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/) [![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

## Описание технической части проекта:

#### 1. Реализовано небольшое API с помощью DRF.

#### 2. Создана модель Gallery, сериализатор, ModelViewSet (с кастомными методами).

#### 3. Создана регистрация, аутентификация по JWT-токену.

#### 4. Созданы для "наглядности" несколько тестов: Модели, права доступа к эндпоинту.

#### 5. Создан дополнительный роут на удаление администратором всех галлерей и изображений в базе.

#### 6. Проект реализован на PostgreSQL

#### 7. Запуск через docker-compose, gunicorn, NGINX

_______________________________________________________________________________________________________________________________________________________________________

### Запуск на локально:

> Клонировать репозиторий git clone https://github.com/AntonDMoskalev/test_DFA.git

> Создать файл .env в корне проекта:

#### .env c дефолтными значениями для более легкого тестирования кода:

> SECRET_KEY=django-insecure-m_$c95i)*)y7r=s^0rp$+##8(2@j^7!o_xo1_=+no&co3ud6%8

> STRIPE_SECRET_KEY=sk_test_4eC39HqLyjWDarjtT1zdp7dc

> STRIPE_PUBLISHABLE_KEY=pk_test_TYooMQauvdEDq54NiTphI7jx

> DB_ENGINE=django.db.backends.postgresql

> DB_NAME=postgres

> POSTGRES_USER=postgres

> POSTGRES_PASSWORD=postgres

> DB_HOST=db

> DB_PORT=5432

### Запуск Docker-compose

> docker-compose up -d

### Провести миграции, создать суперпользователя

> docker-compose exec web python manage.py migrate

> docker-compose exec web python manage.py createsuperuser

_____________________________________________________________________________________________________________________________________________________________________

## Эндпоинты

#### Создание пользователя, получение JWT токена

> api/auth/users/ (POST) {"username": <str>, "password": <str>} - регистрация нового пользователя

> api/auth/users/me/ (GET) - Получить текущего пользователя

> api/auth/jwt/create/ (POST) {"username": <str>, "password": <str>} - Получить токен

> api/auth/jwt/refresh/ (POST) {"token": <refresh token>} - Получить/Востановить токен

#### Эндпоинты для работы с изображениями

> api/auth/gallery/ (GET) - получить список всех изображений, пользователя (для Админ всех изображений всех пользователей)

> api/auth/gallery/ (POST) {"image": <base64>} - добавить изображение (передаётся в Base64 формате) 
Пример(пиксель без изображения): data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7
Пример(картинка): Base64(image).txt

> api/auth/gallery/<id>/ (UPDATE, PUT, DELETE) - CRUD с отдельными объектами

> api/auth/gallery/delete-all-image/ (DELETE) - удалить все изображения из БД (только Админ)


---
### Контакты:
##### [Linkedin](https://www.linkedin.com/in/anton-dev-py/)
##### [Telegram](https://t.me/MoskalevAD)
##### [GitHub](https://github.com/AntonDMoskalev)
