# Практическая работа 5 - Разработка API

## Как сделать чтобы работало?
- В [setting.py](https://github.com/Archive-of-practical-work-for-the-MPT/Django-Educational-Practice/blob/five/coralwave/coralwave/settings.py) настройте подключение к вашей БД
- python -m venv .venv
- .\venv\Scripts\activate
- python manage.py migrate
- python .\manage.py createsuperuser (запроси email и пароль)
- python manage.py runserver
- Открыть в браузере на localhost

## Цель
1. Настроить правила ролей для своего приложения, уровни доступа.

## Демонстрация

<p align="center">
      <img src="https://github.com/user-attachments/assets/9da81396-b495-42c3-8770-0df4d02415e9" alt="Сайт" width="700">
</p>

## Вывод
В ходе работы успешно реализована система разграничения прав доступа на основе ролей для всех разделов веб-приложения. Дополнительно разработано и интегрировано API с ключевыми функциями: пагинацией данных, подключением шаблонов.
