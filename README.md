# Currency Service
## Сервис курса валют

## Описание проекта
### Сервис который отображает курс валюты по отношению к рублю на заданную дату

#### Выводит данные при обращении по адресу в виде:
    http://localhost:8000/rate/?charcode=AUD&date=2024-01-01
#### Результат в виде JSON в формате:
    {
    "charcode": "AUD",
    "date": "2024-01-01",
    "rate": 57.0627
    }


Данные по валютам храниться в базе данных приложения.
А для пополнения этой базы данных написана команда, которая
будет раз в сутки обращаться к сервису ЦБ за актуальными курсами валют по адресу:
    https://www.cbr-xml-daily.ru/daily_json.js

## Стек технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 

---

<details><summary><h2>Адрес проекта</h2></summary>

*(запускается локально)*

    http://127.0.0.1:8000/

> /admin/ # Адрес админки проекта


**Handlers**

```sh
rate/  # Курс валюты

```
</details>

---

<details><summary><h2>Подготовка проекта к запуску</h2></summary>

#### `3` пункт для локального запуска. `4` пункт для ведения разработки

1. *Склонируйте репозиторий и перейдите в него*:

    ```sh
    git clone https://github.com/Oskalovlev/currency_service.git
    ```
    ```sh
    cd currency_service/
    ```
---
2. *Для работы с PostgreSQL* или MySQL*:

    * Создайте в директории `infra/` файл `.env` командой:

        ```sh
        touch infra/.env
        ```
        > Заполните переменные по примеру файла `.env.example`
---
3. *Создайте и активируйте виртуальное окружение*:

    ```sh
    python -m venv venv
    ```
    - Если у вас Linux/macOS
        ```sh
        source venv/bin/activate
        ```

    - Если у вас windows
        ```sh
        source venv/scripts/activate
        ```
---
4. *Обновите pip и установите зависимости*:

    ```sh
    python -m pip install --upgrade pip
    ```
    ```sh
    pip install -r backend/requirements.txt
    ```
</details>

---

<details><summary><h2>Для локального запуска используйте инструкцию</h2></summary>

1. *Выполните миграции*:

    * Инициализируйте миграции (опционально)
        ```sh
        python currency_rate/manage.py migrate
        ```

    * Создайте миграции
        ```sh
        python currency_rate/manage.py makemigrations
        ```

    * Примените миграции
        ```sh
        python currency_rate/manage.py migrate
        ```
---
2. *Создайте суперюзера*:

    ```sh
    python currency_rate/manage.py createsuperuser
    ```

    > Для примера, данные суперюзера:

        username: admin
        mail: admin@admin.ru
        password: admin
        password (again): admin

    > При входе логин указывать с большой буквы `Admin` (если с маленькой не получается зайти)

---

3. *Соберите статику*:
    ```sh
    python currency_rate/manage.py collectstatic --noinput
    ```
---
4. *Локальный запуск*:

    ```sh
    python currency_rate/manage.py runserver
    ```
</details>

---


### Автор

- Оскалов Лев (*Telegram*: [@oskalov](https://t.me/oskalov), **Github**: [Oskalovlev](https://github.com/Oskalovlev))
