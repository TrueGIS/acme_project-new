# Проект ACME

## Стек

- Python 3.14;
- Django 5.2.12.

## Запуск проекта

Создайте и активируйте виртуальное окружение, затем установите зависимости:

```bash
python -m pip install -r requirements.txt
```

Примените миграции и запустите сервер разработки:

```bash
python acme_project/manage.py migrate
python acme_project/manage.py runserver
```

Главная страница будет доступна по адресу `http://127.0.0.1:8000/`, а страница приложения `birthday` — по адресу `http://127.0.0.1:8000/birthday/`.

