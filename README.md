# Практические работы по Django
Репозиторий с практическими работами по учебной практике 3 курса на Django с использованием Python.

Навигация:

* [Практическая работа 1](https://github.com/Archive-of-practical-work-for-the-MPT/Django-Educational-Practice/tree/first) - Разработка главной страницы
* [Практическая работа 2](https://github.com/Archive-of-practical-work-for-the-MPT/Django-Educational-Practice/tree/second) - Создание таблиц
* [Практическая работа 3](https://github.com/Archive-of-practical-work-for-the-MPT/Django-Educational-Practice/tree/third) - Работа с шаблонами
* [Практическая работа 4](https://github.com/Archive-of-practical-work-for-the-MPT/Django-Educational-Practice/tree/four) - Работа с уровнями доступа
* [Практическая работа 5](https://github.com/Archive-of-practical-work-for-the-MPT/Django-Educational-Practice/tree/five) - Разработка API
* [Практическая работа 6](https://github.com/Archive-of-practical-work-for-the-MPT/Django-Educational-Practice) - Деплой проекта на сайте

# Практическая работа 6 - Деплой проекта на сайте

## Описание

Как сделать чтобы работало?
- В [setting.py](https://github.com/Archive-of-practical-work-for-the-MPT/Django-Educational-Practice/blob/six/coralwave/coralwave/settings.py) настройки подключение к вашей БД
- python -m venv .venv
- .\venv\Scripts\activate
- python manage.py migrate
- python .\manage.py createsuperuser (запроси email и пароль)
- python manage.py runserver
- Открыть в браузере на localhost

## Цель

1. Запушить на GitHub.
2. Развернуть на сайте https://www.pythonanywhere.com/

## Демонстрация

<p align="center">
      <img src="https://github.com/user-attachments/assets/e5b63e1c-1224-41e5-8e3e-122574a7e99a" alt="Сайт" width="700">
</p>

## Вывод
В ходе работы проект размещён в репозитории GitHub и [развёрнут](https://merrcurys.pythonanywhere.com) на платформе PythonAnywhere, что подтверждает его работоспособность в production-среде.
