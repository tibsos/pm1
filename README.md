Инструкция по запуску проетка

Скачайте проект

`
git clone https://github.com/tibsos/pm1
`

Создайте и активируйте виртуальную среду

Установите python3 virtual environment


`pip3 install python3-virtualenv`

Создайте виртуальную среду в папке проекта


`python -m venv env
source env/bin/activate`   


Для Windows используйте `env\Scripts\activate`


Установите библиотеки

`
pip install -r requirements.txt
`

Запустите сайт

`python manage.py runserver`
