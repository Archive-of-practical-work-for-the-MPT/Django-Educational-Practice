# Практическая работа 2 - Разработка главной страницы

## Как сделать чтобы работало?
- В [setting.py](https://github.com/Archive-of-practical-work-for-the-MPT/Django-Educational-Practice/blob/second/coralwave/coralwave/settings.py) настройте подключение к вашей БД
- python -m venv .venv
- .\venv\Scripts\activate
- python manage.py migrate
- python .\manage.py createsuperuser (запроси email и пароль)
- python manage.py runserver
- Открыть в браузере на localhost

## Цель
1. Создать 15 таблиц в DRAW.io. 
2. Перенести эти таблички VS Django - мигрировать их в pgAdmin.
3. Добавление, изменение, удаление, детали. 
4. Создание качественного визуала.

## Демонстрация

<p align="center">
      <img src="https://github.com/user-attachments/assets/972879f2-a7ac-494e-807d-ee0f3656e908" alt="Логическая" width="700">
</p>

<p align="center">
      <img src="https://github.com/user-attachments/assets/545fd5fc-9379-4e3f-a874-636e023ee312" alt="Физическая" width="700">
</p>

## Вывод
В ходе выполнения лабораторной работы была разработана структура базы данных, а также создан функционал для работы с ней.
