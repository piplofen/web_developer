# web_developer тестовое
# Инструкция
Используемый стек:
- `python 3.11`
- `django 4.2`
- `psycopg2 2.9.6`

В проекте присутствует `venv`. Библиотеки для работы `venv`:
- `django`
- `psycopg2`
- `pillow`

База данных:
- создаем базу данных с именем `webdeveloper`, используя команду `CREATE DATABASE webdeveloper;`
- создаем пользователя с именем `webdeveloperuser` и паролем `1234`, используя команду `CREATE USER webdeveloperuser WITH PASSWORD '1234';`
- После этого нужно изменить несколько параметров подключения только что созданного пользователя. Это ускорит операции с базой данных (необходимые значения не придется запрашивать и устанавливать при каждом соединении).
```
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```






# План проекта
### 05.04.2023
- [x] создано приложение 
- [x] создана и наполнена база данных
- [x] вывод книжек на страничке
- [x] небольшой дизайн
### 06.04.2023
- [x] разобраться в дизайне
- [x]  добавить в таблицу `Book` столбец `Description`
- [x]  добавить и связать таблицу `Commnents`
- [x]  добавить и связать таблицу `Category`
- [x]  сделать распределение по жанрам
- [x]  добавить изображения книг
- [x]  возможно сделал CRUD в режиме админа
### 07.04.2023
- [x]  сделать открытие книги по кнопке
- [x]  сделать маршрутизацию по всем кнопкам
### 08.04.2023
- сделать форму регистрации и входа
- нормально задизайнить
