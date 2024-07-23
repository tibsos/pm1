Инструкция по запуску проетка

Скачивание проекта

bash
Copy code
git clone https://github.com/tibsos/pm1
cd pm1

Создание и активация виртуальной среды

Установите python3 virtual environment

bash
pip3 install python3-virtualenv

Создайте виртуальную среду

bash
Copy code
python -m venv env
source env/bin/activate   # Для Windows используйте `env\Scripts\activate`
Установите библиотеки

bash
Copy code
pip install -r requirements.txt
Проведите миграцию в базу данных

bash
Copy code
python manage.py migrate

Запустите сайт

bash
Copy code
python manage.py runserver
Сервер будет доступен по адресу http://127.0.0.1:8000/
