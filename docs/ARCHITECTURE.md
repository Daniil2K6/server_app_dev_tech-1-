# 🏗️ Архитектура FAPI_KR1

## Структура проекта

```
FAPI_KR1/
├── app/                      # Основное приложение FastAPI
│   ├── __init__.py           # Инициализация пакета
│   ├── main.py               # Основное приложение и маршруты
│   └── models.py             # Pydantic модели
├── static/                   # Статические файлы
│   ├── index.html            # HTML страница (Задание 1.2)
│   └── test.html             # Интерактивная страница тестирования
├── docs/                     # Документация проекта
│   ├── TESTING.md            # Инструкция по тестированию
│   ├── ARCHITECTURE.md       # Этот файл
│   └── API.md                # (опционально) API документация
├── main.py                   # Entry point для запуска
├── requirements.txt          # Зависимости проекта
├── .gitignore                # Git конфигурация
└── README.md                 # Главная документация
```

---

## Технологический стек

### Backend
- **Python 3.10+** — Язык программирования
- **FastAPI 0.104.1** — Веб-фреймворк для создания API
- **Uvicorn 0.24.0** — ASGI сервер (асинхронный веб-сервер)
- **Pydantic 2.5.0** — Валидация данных и парсинг

### Frontend
- **HTML5** — Разметка
- **CSS3** — Стили
- **JavaScript (Vanilla)** — Интерактивность без фреймворков
- **Fetch API** — Асинхронные запросы к API

---

## Архитектурная диаграмма

```
┌─────────────────────────────────────────────────────────────┐
│                     HTTP Client (Browser)                   │
└────────────────────────┬────────────────────────────────────┘
                         │ Requests/Responses
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Uvicorn ASGI Server                        │
│                   (localhost:8000)                            │
└────────────────────────┬────────────────────────────────────┘
                         │
            ┌────────────┴────────────┐
            ▼                         ▼
    ┌──────────────┐        ┌──────────────┐
    │ Static Files │        │  FastAPI App │
    │  (HTML/CSS)  │        │              │
    └──────────────┘        └──────┬───────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
            ┌────────────┐  ┌────────────┐  ┌────────────┐
            │  Routes    │  │  Models    │  │  Storage   │
            │ (app.main) │  │ (Pydantic) │  │   (RAM)    │
            └────────────┘  └────────────┘  └────────────┘
```

---

## Компоненты системы

### 1. **Точка входа (main.py)**
```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:main_app", ...)
```
- Запускает ASGI сервер Uvicorn
- Загружает приложение FastAPI из модуля app
- Слушает на localhost:8000

### 2. **Приложение FastAPI (app/main.py)**
```python
from fastapi import FastAPI
main_app = FastAPI(title="FAPI_KR1", version="1.0.0")
```
- Основное приложение с маршрутами
- 7 маршрутов (endpoints) для 7 заданий
- Хранилище данных в памяти (feedbacks список)

### 3. **Модели данных (app/models.py)**
```python
class User(BaseModel):
    name: str
    id: int

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
```
- Pydantic модели для валидации
- Автоматическая проверка типов и ограничений
- Генерация JSON Schema для Swagger

### 4. **Маршруты (Routes)**

#### Простые маршруты (без параметров)
```python
@main_app.get("/")
def read_root():
    return {"message": "..."}
```

#### Маршруты с параметрами
```python
@main_app.post("/calculate")
def calculate(num1: float, num2: float):
    return {"result": num1 + num2}
```

#### Маршруты с телом запроса (Body)
```python
@main_app.post("/feedback")
def submit_feedback(feedback: Feedback):
    feedbacks.append({...})
    return {"message": "..."}
```

#### Маршруты со статическими файлами
```python
@main_app.get("/html")
def read_html():
    return FileResponse(html_path)
```

---

## Поток данных

### Пример: Отправка отзыва

```
1. JavaScript fetch() → HTTP POST запрос
   {
     "name": "Мария",
     "message": "Отзыв текст..."
   }

2. → Uvicorn получает запрос
   → Роутер FastAPI находит подходящий handler

3. → Pydantic парсит JSON в объект Feedback
   → Валидирует:
     - name (2-50 символов)
     - message (10-500 символов)
     - Проверяет на запретные слова

4. → Если валидация OK:
   └─→ submit_feedback() добавляет в feedbacks
       └─→ Возвращает успешный ответ

   → Если валидация FAIL:
   └─→ FastAPI автоматически вернёт 422 ошибку
       с описанием проблемы

5. ← HTTP 200 с JSON ответом
   → JavaScript обновляет страницу
```

---

## Маршруты и их функции

| Номер | Метод | Маршрут | Функция | Model |
|-------|-------|---------|---------|-------|
| 1.1 | GET | `/` | Возвращает JSON приветствие | - |
| 1.2 | GET | `/html` | Возвращает HTML файл | - |
| 1.3 | POST | `/calculate` | Сумма двух чисел | - |
| 1.4 | GET | `/users` | Возвращает User | User |
| 1.5 | POST | `/user` | Проверка возраста | UserAge → UserAgeResponse |
| 2.1 | POST | `/feedback` | Сохраняет отзыв | Feedback |
| 2.2 | POST | `/feedback` | Валидирует отзыв | Feedback (с rules) |

### Дополнительные маршруты

- `GET /feedbacks` — Просмотр всех сохранённых отзывов
- `GET /test` — Интерактивная страница тестирования
- `GET /docs` — Swagger UI (автоматически)
- `GET /redoc` — ReDoc (автоматически)

---

## Жизненный цикл приложения

```
1. Запуск: python main.py
   ↓
2. uvicorn создаёт сервер
   ↓
3. FastAPI инициализирует приложение
   ↓
4. Загружаются маршруты (routes)
   ↓
5. Генерируется OpenAPI schema (Swagger)
   ↓
6. Сервер слушает на localhost:8000
   ↓
7. Клиент отправляет HTTP запрос
   ↓
8. FastAPI роутер находит подходящий handler
   ↓
9. Pydantic валидирует данные
   ↓
10. Handler обрабатывает запрос
    ↓
11. Возвращается JSON ответ
    ↓
12. Клиент получает ответ
```

---

## Хранилище данных

### In-Memory Storage (Оперативная память)

```python
# Файл: app/main.py
feedbacks = []  # Список отзывов
current_user = User(name="Дарья Невская", id=1)  # Текущий пользователь
```

**Важно:** Данные сохраняются только в памяти программы:
- ✅ Быстро
- ✅ Просто
- ❌ Теряются при перезапуске сервера
- ❌ Не подходит для production

Для production нужна база данных (PostgreSQL, MongoDB, etc.)

---

## Обработка ошибок

### Валидация Pydantic

```
Неправильный формат JSON
  ↓
Pydantic выбрасывает ошибку
  ↓
FastAPI автоматически возвращает 422 Unprocessable Entity
  ↓
Ответ содержит описание ошибок
```

**Пример ошибки валидации:**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "name"],
      "msg": "String should have at least 2 characters",
      "input": "A"
    }
  ]
}
```

### Запретные слова

```python
@field_validator('message')
@classmethod
def validate_message(cls, v):
    forbidden = ['кринж', 'рофл', 'вайб']
    if any(word in v.lower() for word in forbidden):
        raise ValueError('Использование недопустимых слов')
    return v
```

---

## API Документация (Swagger)

**Автоматически генерируется FastAPI:**

- `GET /docs` → Swagger UI (интерактивный)
- `GET /redoc` → ReDoc (красивый)
- `GET /openapi.json` → OpenAPI schema (JSON)

Документация содержит:
- ✅ Описание всех маршрутов
- ✅ Типы параметров
- ✅ Примеры запросов/ответов
- ✅ Интерактивное тестирование

---

## Безопасность

### Текущие уровни защиты

- ✅ Валидация входных данных (Pydantic)
- ✅ Проверка типов данных
- ✅ Ограничение длины строк
- ✅ Фильтрация запретных слов

### Что НЕ реализовано (для production нужно)

- ❌ CORS (кроссдоменные запросы)
- ❌ Аутентификация (JWT)
- ❌ Шифрование данных
- ❌ Rate limiting
- ❌ SQL injection protection (т.к. нет БД)

---

## Производительность

### Текущие характеристики

- **Одновременные подключения:** ~100 (зависит от OS)
- **Время обработки запроса:** < 1ms
- **Используемая память:** ~50-100 MB при запуске

### Лимитирующие факторы

- Одноядерный Uvicorn процесс
- In-memory хранилище
- Отсутствие кеширования

### Улучшения для production

- Использовать Gunicorn + Uvicorn (multiprocess)
- Кешировать часто запрашиваемые данные
- Использовать Redis для сессий
- Добавить database connection pooling
