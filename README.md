# E-Learning Platform API

Этот API разработан для виртуальной образовательной платформы, предоставляющей доступ к урокам, статистике и продуктам. Платформа предоставляет информацию о статусе уроков, времени просмотра и позволяет администраторам отслеживать статистику продуктов.

## Требования

Перед использованием этого API убедитесь, что у вас установлены следующие зависимости:

- Python 3.9 и выше
- Django
- Django REST framework
- Другие зависимости, указанные в `requirements.txt`

## Установка

Для установки выполните следующие шаги:

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/andrewdya/elearning-platform-api.git

2. **Перейдите в папку:**
   ```bash
   cd elearning\


3. **Запустите сервер Django:**
   ```bash
   python manage.py runserver


Теперь API запущен и доступен по следующим адресам:

- [http://127.0.0.1:8000/api/product-stats/](http://127.0.0.1:8000/api/product-stats/)
- [http://127.0.0.1:8000/api/lessons/by-user/](http://127.0.0.1:8000/api/lessons/by-user/)
- [http://127.0.0.1:8000/api/lessons/by-product/](http://127.0.0.1:8000/api/lessons/by-product/)
