# CRM-системы

Для успешного запуска проекта на Django с использованием PostgreSQL необходимо расписать каждую деталь от создания базы данных до выполнения миграций и отображения данных. В этом пошаговом руководстве будут включены все команды, SQL-запросы и скриншоты консоли.


## 1. Установка и настройка окружения

### 1.1. Установка Python и PostgreSQL

Убедитесь, что на вашей машине установлены:

- **Python**: версия 3.10 или выше.
- **PostgreSQL**: Проверьте с помощью команд:

  ```bash
  python3 --version
  psql --version


### 1.2. Установка зависимостей

1. Создайте виртуальное окружение:
   - `python3 -m venv myenv`
2. Активируйте виртуальное окружение:
   - `source myenv/bin/activate` (для Linux/macOS) или `myenv\Scripts\activate` (для Windows)
3. Установите необходимые зависимости:
   - `pip install django psycopg2-binary`
     - **Django**: основной фреймворк для создания веб-приложений.
     - **psycopg2-binary**: драйвер для работы с базой данных PostgreSQL.


## 2. Создание базы данных

### 2.1. Создание базы данных и пользователя PostgreSQL

1. Войдите в консоль PostgreSQL:
   - `psql -U postgres`

2. Выполните команды для создания базы данных и пользователя:
   - `CREATE DATABASE crm_system;`
   - `CREATE USER crm_user WITH PASSWORD 'crm_password';`
   - `GRANT ALL PRIVILEGES ON DATABASE crm_system TO crm_user;`

3. Проверка результата:
   Чтобы увидеть созданную базу данных, выполните команду:
   - `\l`

Пример вывода:

 Name        | Owner    | Encoding | Collate | Ctype   | Access privileges
-------------+----------+----------+---------+---------+-------------------
 crm_system  | crm_user | UTF8     | en_US   | en_US   |


### 3. Настройка Django проекта

3.1. Создание проекта и приложения

1. Для создания нового Django проекта выполните команду:
   - `django-admin startproject crm_system .`
   Данная команда создаст структуру проекта с именем `crm_system` в текущей директории.
2. Для создания нового приложения выполните команду:
   - `python3 manage.py startapp crm`


### 3.2. Настройка базы данных в `settings.py`

Откройте файл `crm_system/settings.py` и найдите раздел, который отвечает за настройки базы данных. Замените его содержимое на следующее, чтобы указать параметры подключения к PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crm_system',  # Имя базы данных
        'USER': 'crm_user',  # Имя пользователя
        'PASSWORD': 'crm_password',  # Пароль пользователя
        'HOST': 'localhost',  # Адрес хоста базы данных
        'PORT': '5432',  # Порт базы данных PostgreSQL
    }
}


4. Модели и миграции

4.1. Создание моделей
В файле crm/models.py создайте необходимые модели:

from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


4.2. Генерация миграций

Выполните команды для создания и применения миграций:
python3 manage.py makemigrations crm
python3 manage.py migrate
Пример вывода консоли:

Migrations for 'crm':
  crm/migrations/0001_initial.py
    - Create model Service
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, crm, sessions
Running migrations:
  Applying crm.0001_initial... OK


4.3. Проверка таблиц в PostgreSQL
Подключитесь к базе данных:  psql -U crm_user -d crm_system
Посмотрите список таблиц:  \d

Пример вывода:

                  List of relations
 Schema |           Name            |   Type   |  Owner
--------+---------------------------+----------+----------
 public | crm_service               | table    | crm_user
 public | django_migrations         | table    | crm_user
 public | django_content_type       | table    | crm_user


Посмотрите структуру таблицы:\d crm_service


                                     Table "public.crm_service"
   Column   |          Type          | Collation | Nullable |              Default
------------+------------------------+-----------+----------+-----------------------------------
 id         | integer                |           | not null | nextval('crm_service_id_seq'::regclass)
 name       | character varying(100) |           | not null |
 description| text                   |           | not null |
 price      | numeric(10,2)          |           | not null |
Indexes:
    "crm_service_pkey" PRIMARY KEY, btree (id)


5. Заполнение данных
5.1. Через админку
Зарегистрируйте модель в crm/admin.py:

from django.contrib import admin
from .models import Service

admin.site.register(Service)


Создайте суперпользователя:
python3 manage.py createsuperuser
Запустите сервер:  python3 manage.py runserver

Перейдите в админку http://127.0.0.1:8000/admin, войдите и добавьте услуги.


5.2. Через SQL
Добавьте данные в таблицу:
INSERT INTO crm_service (name, description, price) VALUES 
('Разработка сайта', 'Создание сайта под ключ', 15000),
('SEO-продвижение', 'Оптимизация сайта для поисковых систем', 10000);


Проверьте данные:
SELECT * FROM crm_service;

Пример вывода:

 id |       name        |         description          | price
----+-------------------+------------------------------+--------
  1 | Разработка сайта  | Создание сайта под ключ      | 15000
  2 | SEO-продвижение   | Оптимизация сайта            | 10000


6. Вывод данных на страницу
Создайте представление и маршрут для отображения данных:
views.py

from django.shortcuts import render
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})


urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.service_list, name='service_list'),
]

templates/service_list.html
<!DOCTYPE html>
<html>
<head>
    <title>Список услуг</title>
</head>
<body>
    <h1>Услуги</h1>
    <ul>
        {% for service in services %}
            <li>{{ service.name }} - {{ service.price }} руб.</li>
        {% endfor %}
    </ul>
</body>
</html>


7. Проверка работы
Перейдите по адресу http://127.0.0.1:8000/services/ и убедитесь, что данные отображаются.


Примеры
7.1.	Консоль создания базы данных:

CREATE DATABASE crm_system;
CREATE USER crm_user WITH PASSWORD 'crm_password';
GRANT ALL PRIVILEGES ON DATABASE crm_system TO crm_user;


7.2.	Пример миграции:

Applying crm.0001_initial... OK

7.3.	Результат SQL-запросов:

SELECT * FROM crm_service;
id | name               | description                   | price
---+--------------------+-------------------------------+-------
1  | Разработка сайта   | Создание сайта под ключ       | 15000