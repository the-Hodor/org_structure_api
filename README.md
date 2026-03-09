# Organization Structure API

REST API для управления иерархической структурой организации: отделами и сотрудниками.

## Технологический стек

* Python 3.10
* Django
* Django REST Framework
* PostgreSQL
* Docker / Docker Compose

## Возможности

* Управление организациями
* Иерархические отделы (древовидная структура)
* Управление сотрудниками
* Перемещение отдела внутри иерархии
* Защита от циклических зависимостей в дереве отделов
* Endpoint для получения структуры организации (представление в виде дерева)

## Структура проекта

```
org_structure_api/
│
├── config/ # Настройки Django проекта
│
├── organizations/ # Основное приложение
│ ├── api/ # API слой (views, serializers, urls)
│ ├── services/ # Бизнес-логика
│ ├── models.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── manage.py
└── README.md

```
## Запуск с Docker

### 1. Клонировать репозиторий


git clone https://github.com/the-Hodor/org_structure_api.git  
cd org_structure_api


## 2. Создание файла окружения

Необходимо создать файл `.env` на основе файла `.env.example`.

### Linux / macOS

```bash
cp .env.example .env
```

### Windows (PowerShell)

```powershell
copy .env.example .env
```

После копирования в файле `.env` будут указаны параметры подключения к базе данных:

```
DB_NAME=organization_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```


### 3. Запустить контейнеры


docker-compose up --build


### 4. Применить миграции


docker-compose exec web python manage.py migrate


### 5. Создать суперпользователя


docker-compose exec web python manage.py createsuperuser


### 6. Открыть API


http://127.0.0.1:8000/api/


Админ-панель:


http://127.0.0.1:8000/admin/


## API Endpoints

### Organizations


GET /api/organizations/
POST /api/organizations/


Структура организации:


GET /api/organizations/{id}/structure/


Возвращает полное дерево отделов вместе с сотрудниками.

### Departments


GET /api/departments/
POST /api/departments/


Перемещение отдела:


POST /api/departments/{id}/move/


Пример тела запроса:


{
"parent": 2
}


### Employees


GET /api/employees/
POST /api/employees/


## Бизнес-логика

Операции с отделами обрабатываются через сервисный слой:


organizations/services/


Это позволяет отделить бизнес-логику от API слоя.

При перемещении отделов реализована защита от циклов, чтобы предотвратить создание некорректных иерархических структур.

## Примечания

Проект использует PostgreSQL в качестве основной базы данных и Docker для воспроизводимого окружения разработки.

Если хочешь, я ещё могу:

подправить README так, чтобы он выглядел более профессионально для GitHub (как у настоящих open-source проектов),

или добавить секции "Installation", "Usage", "Architecture", "Future Improvements", чтобы он выглядел сильнее для работодателей.
