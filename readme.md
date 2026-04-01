# Микросервис для сокращения ссылок

Сервис для сокращения ссылок на FastAPI

## Стек

- **FastAPI** — основной фреймворк
- **PostgreSQL** — хранение ссылок и статистики
- **SQLAlchemy (async)** — работа с БД
- **Alembic** — миграции
- **Poetry** — управление зависимостями
- **Docker / docker-compose** — запуск окружения

---

## Эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| `POST` | `/shorten` | Создать короткую ссылку |
| `GET` | `/{short_id}` | Редирект на оригинальную ссылку |
| `GET` | `/stats/{short_id}` | Получить количество переходов |

---

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <repo_url>
cd <repo_name>
```

### 2. Создать `.env` файл

```bash
cp .env.example .env
```

Заполнить `.env`, например:

```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db:5432
DB_NAME=shortener
```

### 3. Запустить через docker-compose

```bash
docker-compose up -d --build
```

Сервис будет доступен на `http://localhost:7893`

Swagger UI доступен на `http://localhost:7893/docs`
