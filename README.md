# TenderTracker 
Микросервис трекинга статуса тендеров


## Запуск через Docker (рекомендуемый способ)

1. Установите Docker.
2. Склонируйте репозиторий:
git clone https://github.com/Artmen1989/TenderTracker.git
cd TenderTracker
3. Запустите контейнеры:
docker-compose up --build
4. После запуска откройте браузер: [http://localhost:8000/docs](http://localhost:8000/docs)
5. В Swagger UI вы сможете протестировать все эндпоинты. Тестовые данные создаются автоматически.

## Локальный запуск (без Docker)

1. Установите PostgreSQL и создайте базу `tender_db` (логин/пароль `postgres`/`0000`).
2. Установите зависимости: `pip install -r requirements.txt`
3. Примените миграции: `alembic upgrade head`
4. Запустите сервер: `uvicorn app.main:app --reload`
5. Для заполнения тестовыми данными выполните: `python seed.py`