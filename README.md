**API-сервис для вопросов и ответов**

Проект для формирования API сервиса. В проекте испольуются 2 модели:

**Question** – вопрос:

id: int

text: str (текст вопроса)

created_at: datetime


**Answer** – ответ на вопрос:

id: int

question_id: int (ссылка на Question)

user_id: str (идентификатор пользователя, формат - uuid)

text: str (текст ответа)

created_at: datetime

Проект включает в себя следующие endpoints:

Для **Questions**:

**GET** /questions/ — список всех вопросов

**POST** /questions/ — создать новый вопрос. Запрос состоит из: Тело запроса: {"text": Required, "created_at": Optional}

**GET** /questions/{id} — получить вопрос и все ответы на него. Запрос состоит из: Параметр пути: id вопроса

**DELETE** /questions/{id} — удалить вопрос (вместе с ответами). Запрос состоит из: Параметр пути: id вопроса

Для **Answers**:

**POST** /questions/{id}/answers/ — добавить ответ к вопросу. Запрос состоит из: Параметр пути: id вопроса, Тело запроса: {"text": Required, "created_at": Optional, "user_id": Required (в формате uuid, пример - e9c637b1-3f57-4eda-88ad-ccd4b7b1a102}

**GET** /answers/{id} — получить конкретный ответ. Запрос состоит из: Параметр пути: id ответа

**DELETE** /answers/{id} — удалить ответ. Запрос состоит из: Параметр пути: id ответа

Сервис поддерживает следующий **функционал**:

1 - При обращении к API выполняется алгоритм в зависимости от используемого маршрута и метода;

2 - Нельзя создать ответ к несуществующему вопросу;

3 - Один и тот же пользователь может оставлять несколько ответов на один вопрос;

4 - При удалении вопроса должны удаляться все его ответы (каскадно).

Стек:

1 - Django

2 - DRF

3 - PostgreSQL

4 - Docker-compose

Для логгирования используется встроенный инструмент в **Django logging**. Тестирование произведено в модуле **tests**, используя встроенный функционал на основе **unittest**, а также ручное тестирование с помощью инструмента **postman**.

Для проверки производительности используемой структуры запросов используется инструмент **django-silk**, который позволяет узнать количество выполняемых запросов для получения результата, а также время выполнения запросов (зависит от технического функционла ПК)

<img width="1830" height="927" alt="image" src="https://github.com/user-attachments/assets/91934997-70d7-4d78-9e06-0ded5ce696d4" />

**Запуска сервиса**

Первоначально нужно создать файл *.env в корне проекта, в нём указать следующие данные:

secret_key=ключ к приложению

DATABASE_NAME=наименование базы

DATABASE_USER=имя пользователя

DATABASE_PASSWORD=пароль

DATABASE_HOST=хост

DATABASE_PORT=порт

Запуск: docker-compose up -d

В сервисе используется bash скрипт, который выполняет миграции и запускает сервис. Его инициализация прописана в Dockerfile, где также указана логика формирования образа для API сервиса с установкой всех зависимостей.
Так как в docker-compose используется два контейнера (web-service и postgres) то в настройках Django db host указан наименованием контейнера (pgdb). Если запускать только сервис без бд, то нужно поменять на используемый хост.

Примеры обращения на endpoints:

GET /questions/

<img width="1374" height="729" alt="image" src="https://github.com/user-attachments/assets/c6777832-eecd-4b71-8e4b-f13fc36c7b7d" />

POST /questions/

<img width="1378" height="531" alt="image" src="https://github.com/user-attachments/assets/0ff3afdb-3c42-4e70-a793-61d5d2261ff8" />

POST /questions/ с некорректной датой

<img width="1378" height="535" alt="image" src="https://github.com/user-attachments/assets/da72e83a-7e08-496c-a139-c79b4e864182" />

GET /questions/{id}

<img width="1382" height="816" alt="image" src="https://github.com/user-attachments/assets/4168b506-ba9b-4979-9b3b-06f9127d0bbf" />

GET /questions/{id} с несуществующим ID

<img width="1381" height="457" alt="image" src="https://github.com/user-attachments/assets/7618523c-a2a6-4671-807b-d3858ef4fb30" />

DELETE /questions/{id}

<img width="1379" height="511" alt="image" src="https://github.com/user-attachments/assets/ef3835b8-43cd-4cf7-aa15-59f84c14b200" />

POST /questions/{id}/answers/

<img width="1371" height="599" alt="image" src="https://github.com/user-attachments/assets/164324aa-a45b-4b68-8249-b422bf302314" />

POST /questions/{id}/answers/ без параметра user_id

<img width="1365" height="532" alt="image" src="https://github.com/user-attachments/assets/8eddfc7e-79b6-430e-97c9-5584770b5a21" />

GET /answers/{id}

<img width="1369" height="570" alt="image" src="https://github.com/user-attachments/assets/3a63d6a2-bc8f-4f0e-ac88-8b86944c3f35" />

GET /answers/{id} с несуществующим ID

<img width="1372" height="515" alt="image" src="https://github.com/user-attachments/assets/23f9b492-ffdf-4311-bd4a-75a5affd1a4a" />


DELETE /answers/{id}

<img width="1372" height="588" alt="image" src="https://github.com/user-attachments/assets/f8a22f3c-a9b9-4328-bf42-113c26f7bffc" />
