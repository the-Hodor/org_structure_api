# Organization Structure API

REST API для управления организационной структурой компании: организациями, департаментами и сотрудниками.

## Стек технологий

* Python 3.10
* Django
* Django REST Framework
* PostgreSQL
* Docker / Docker Compose
* Swagger (drf-spectacular)

---

# Функциональность

* управление организациями
* иерархическая структура департаментов
* управление сотрудниками
* перемещение департаментов внутри структуры
* защита от циклов в дереве департаментов
* получение структуры организации

---

# Запуск проекта

## 1. Клонировать репозиторий

```bash
git clone <repo_url>
cd org_structure_api
```

---

## 2. Создать файл окружения

Создайте файл `.env` на основе `.env.example`.

### Linux / macOS

```bash
cp .env.example .env
```

### Windows (PowerShell)

```powershell
copy .env.example .env
```

Файл `.env` должен содержать:

```
DB_NAME=organization_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

---

## 3. Запуск контейнеров

```bash
docker-compose up --build
```

Будут запущены:

* Django API
* PostgreSQL

---

## 4. Применить миграции

Откройте новый терминал и выполните:

```bash
docker-compose exec web python manage.py migrate
```

---

## 5. Создать администратора

```bash
docker-compose exec web python manage.py createsuperuser
```

---

# Доступ к приложению

### API

```
http://127.0.0.1:8000/api/
```

### Swagger документация

```
http://127.0.0.1:8000/api/docs/
```

Через Swagger можно:

* просмотреть все endpoints
* увидеть структуру запросов
* протестировать API прямо в браузере

---

### Админ панель

```
http://127.0.0.1:8000/admin/
```

---

# Основные endpoints

## Organizations

```
GET /api/organizations/
POST /api/organizations/
GET /api/organizations/{id}/structure/
```

---

## Departments

```
GET /api/departments/
POST /api/departments/
GET /api/departments/{id}/
PATCH /api/departments/{id}/
DELETE /api/departments/{id}/
POST /api/departments/{id}/move/
```

---

## Employees

```
GET /api/employees/
POST /api/employees/
GET /api/employees/{id}/
PATCH /api/employees/{id}/
DELETE /api/employees/{id}/
```

---

# Архитектура

Бизнес-логика вынесена в сервисный слой:

```
organizations/services/
```

Это позволяет отделить API слой от бизнес-логики.

---

# Особенности реализации

* защита от циклических зависимостей в структуре департаментов
* кастомный endpoint для перемещения департаментов
* использование PostgreSQL
* контейнеризация с Docker
* автоматическая документация API через Swagger

