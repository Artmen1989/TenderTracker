**TenderTracker** — это RESTful API-сервис на FastAPI для управления тендерами и отслеживания их статусов.  
Каждое изменение статуса логируется с указанием пользователя, времени и причины.

## 🚀 Возможности
- Создание тендера (статус по умолчанию — `draft`)
- Обновление статуса: `draft` → `active` → `won` / `lost`
- Получение информации о тендере
- Получение списка тендеров с пагинацией и фильтром по статусу
- История изменений статуса с указанием пользователя и причины
- Хранение данных в PostgreSQL, управление миграциями через Alembic

---

## 🐳 Запуск через Docker (рекомендуемый способ)

1. Убедитесь, что у вас установлены **Docker** и **Docker Compose**.
2. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/Artmen1989/TenderTracker.git
   cd TenderTracker
   ```
3. Запустите контейнеры:
   ```bash
   docker-compose up --build
   ```
4. Откройте в браузере: [http://localhost:8000/docs](http://localhost:8000/docs)

После запуска автоматически применяются миграции.  
Тестовые данные можно создать вручную через Swagger или выполнить скрипт:
```bash
docker exec -it tender_app python seed.py
```

---

## 💻 Локальный запуск (без Docker)

### Требования
- Python 3.10+
- PostgreSQL (локально или удалённо)
- Установленный `psql` (опционально)

### Инструкция
1. Клонируйте репозиторий и создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Создайте базу данных `tender_db` в PostgreSQL.
4. Скопируйте `.env.example` в `.env` и укажите строку подключения:
   ```
   DATABASE_URL=postgresql://user:pass@localhost:5432/tender_db
   ```
5. Примените миграции:
   ```bash
   alembic upgrade head
   ```
6. Запустите сервер:
   ```bash
   uvicorn app.main:app --reload
   ```
7. Откройте [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠️ Технологии
- **FastAPI** — веб-фреймворк
- **SQLAlchemy** — ORM
- **PostgreSQL** — СУБД
- **Alembic** — миграции
- **Docker** & **Docker Compose** — контейнеризация

---

## 📁 Структура проекта
```
TenderTracker/
├── app/
│   ├── routers/          # Эндпоинты
│   ├── models.py         # SQLAlchemy модели
│   ├── schemas.py        # Pydantic схемы
│   ├── crud.py           # Операции с БД
│   ├── history.py        # Логирование истории
│   ├── dependencies.py   # Зависимости (X-User-ID)
│   ├── database.py       # Подключение к БД
│   └── main.py           # Точка входа FastAPI
├── migrations/           # Миграции Alembic
├── tests/                # Тесты (pytest)
├── docker-compose.yml
├── Dockerfile
├── seed.py               # Скрипт заполнения тестовыми данными
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📄 Лицензия
MIT © 2025 [Artmen1989](https://github.com/Artmen1989)