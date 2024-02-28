# Django CRM API

## Обзор

Задача - создать простую систему управления запасами продуктов. Система должна позволять пользователям добавлять, обновлять, удалять и перечислять заведения и продукты в инвентаре.

# Запуск проекта Django:


1. Создайте виртуальную среду (необязательно, но рекомендуется):


   python -m venv venv

3. Активируйте виртуальную среду:


    venv\Scripts\activate

4. Установите зависимости:


    pip install -r requirements.txt

5. Запустите миграцию:
    

    python manage.py makemigrations
    python manage.py migrate

6. Создайте суперпользователя 


    python manage.py createsuperuser

7. Запустите сервер разработки Django:


    python manage.py runserver
    


## Документация Swagger

  - [Конечные точки API](http://127.0.0.1:8000/api/swagger/)
  - [Список продуктов](http://127.0.0.1:8000/api/crm/products/)
  - [Список магазинов](http://127.0.0.1:8000/api/crm/stores/)

## Создание и запуск с помощью Docker Compose
1. Клонируем репозиторий:


    git-клон https://github.com/your-username/django-crm-api.git

    cd django-crm-api


2. Создайте и запустите приложение с помощью Docker Compose:
    

    docker-compose up --build

Эта команда создаст образы Docker и запустит контейнеры. Приложение должно быть доступно по адресу http://localhost:8000/.

