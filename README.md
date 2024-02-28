# Django CRM API

## Обзор

Цель - создать простую систему управления запасами продуктов. Система должна позволять пользователям добавлять, обновлять, удалять и перечислять заведения и продукты в инвентаре.

# Запуск проекта Django:

1. Создайте виртуальное окружение (необязательно, но рекомендуется):

    ```bash
    python -m venv venv
    ```

2. Активируйте виртуальное окружение:

    ```bash
    venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Запустите миграции:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Создайте суперпользователя:

    ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер разработки Django:

    ```bash
    python manage.py runserver
    ```

## Документация Swagger

  - [Конечные точки API](http://127.0.0.1:8000/api/swagger/)
  - [Список продуктов](http://127.0.0.1:8000/api/crm/products/)
  - [Список магазинов](http://127.0.0.1:8000/api/crm/stores/)

## Создание и запуск с помощью Docker Compose

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/your-username/django-crm-api.git

    cd django-crm-api
    ```

2. Создайте и запустите приложение с помощью Docker Compose:

    ```bash
    docker-compose up --build
    ```

    Эта команда создаст образы Docker и запустит контейнеры. Приложение должно быть доступно по адресу http://localhost:8000/.
