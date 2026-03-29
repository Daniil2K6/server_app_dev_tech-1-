# 📚 FAPI_KR1 - Контрольная работа №1 по FastAPI

![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![Uvicorn](https://img.shields.io/badge/Uvicorn-0.24.0-purple?style=flat-square)
![Pydantic](https://img.shields.io/badge/Pydantic-2.5.0-orange?style=flat-square)

## 🎯 Описание проекта

На решение **7 заданий** контрольной работы №1 по курсу "Технологии Серверных Приложений" с использованием:

- **FastAPI** - современный фреймворк для создания REST API на Python
- **Pydantic** - валидация данных и типизация
- **Uvicorn** - ASGI сервер для запуска приложения

**Все 7 заданий реализованы и протестированы ✅**

---

## 📁 Структура проекта

```
FAPI_KR1_NEW/
│
├── src/                          # Исходный код приложения
│   ├── __init__.py              # Инициализация пакета src
│   ├── app.py                   # Основное FastAPI приложение (маршруты)
│   ├── models.py                # Pydantic модели для валидации
│   │
│   ├── templates/               # HTML шаблоны
│   │   ├── index.html          # HTML страница для Задания 1.2
│   │   └── test.html           # Интерактивная страница тестирования
│   │
│   └── static/                  # Статические файлы (CSS, JS, images)
│       └── (пустая - для будущих файлов)
│
├── docs/                         # Документация проекта
│   └── (пустая - для будущих файлов)
│
├── main_run.py                  # 🚀 Точка входа - запуск приложения
├── requirements.txt             # Зависимости Python
├── README.md                    # Этот файл
└── .gitignore                   # Исключение файлов из Git
```

---

## 📋 Описание файлов и их назначение

| Файл | Расположение | Назначение | Задания |
|------|-------------|-----------|---------|
| **app.py** | `src/` | Основное приложение FastAPI со всеми маршрутами (endpoints) | 1.1-2.2 |
| **models.py** | `src/` | Pydantic модели: User, UserAge, UserAgeResponse, Feedback | 1.4, 1.5, 2.1-2.2 |
| **index.html** | `src/templates/` | HTML страница "Я ОБОЖАЮ ВСТАВАТЬ К ПЕРВОЙ ПАРЕ :)" | 1.2 |
| **test.html** | `src/templates/` | Красивый интерактивный UI для тестирования всех маршрутов | Тестирование |
| **main_run.py** | Корень проекта | Скрипт запуска приложения на порте 8000 | - |
| **requirements.txt** | Корень проекта | Список зависимостей Python (fastapi, uvicorn, pydantic) | - |

---

## 🚀 Быстрый старт

### 1️⃣ Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2️⃣ Запуск приложения

```bash
python3 main_run.py
```

**Сервер запустится по адресу:** `http://localhost:8000`

Вывод в консоли:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

### 3️⃣ Тестирование

Открой в браузере одну из ссылок:

- 🧪 **Интерактивное тестирование:** http://localhost:8000/test
- 📚 **Swagger документация:** http://localhost:8000/docs
- 🔄 **ReDoc документация:** http://localhost:8000/redoc

---

## 📝 Описание всех 7 заданий

### 📌 Задание 1.1 - GET / (JSON приветствие)

**Маршрут:** `GET /`

**Описание:** Возвращает JSON объект с приветствием. Должен поддерживать авторелоад при изменении кода.

**Ответ:**
```json
{
  "message": "Авторелоад действительно работает"
}
```

**Тест:** Откройи http://localhost:8000/ или нажми кнопку "Тест" на странице тестирования

---

### 📌 Задание 1.2 - GET /html (HTML страница)

**Маршрут:** `GET /html`

**Описание:** Возвращает HTML страницу с текстом "Я ОБОЖАЮ ВСТАВАТЬ К ПЕРВОЙ ПАРЕ :)"

**Файл:** `src/templates/index.html`

**Тест:** Откройи http://localhost:8000/html или нажми "Открыть" на странице тестирования

---

### 📌 Задание 1.3 - POST /calculate (Сумма чисел с валидацией)

**Маршрут:** `POST /calculate`

**Параметры:** Query параметры
- `num1` (float) - первое число
- `num2` (float) - второе число

**Ответ:**
```json
{
  "result": 15.5
}
```

**Примеры запросов:**
```bash
# curl
curl -X POST "http://localhost:8000/calculate?num1=10&num2=5.5"

# JavaScript (на странице тестирования)
# Введи 10 в "Первое число" и 5.5 в "Второе число", нажми "Тест"
```

**Особенность:** Задание 2.2 требует валидации, поэтому если отправить неправильные параметры, получишь HTTP 422 с ошибкой валидации (это нормально!)

---

### 📌 Задание 1.4 - GET /users (User модель)

**Маршрут:** `GET /users`

**Описание:** Возвращает данные пользователя используя Pydantic модель User

**Ответ:**
```json
{
  "name": "Дарья Невская",
  "id": 1
}
```

**Модель** (в `src/models.py`):
```python
class User(BaseModel):
    name: str
    id: int
```

**Тест:** http://localhost:8000/users или нажми "Тест" на странице тестирования

---

### 📌 Задание 1.5 - POST /user (Проверка совершеннолетия)

**Маршрут:** `POST /user`

**Описание:** Проверяет возраст пользователя и возвращает флаг is_adult (true если возраст >= 18)

**Входные данные** (JSON):
```json
{
  "name": "Иван",
  "age": 25
}
```

**Ответ:**
```json
{
  "name": "Иван",
  "age": 25,
  "is_adult": true
}
```

**Модели** (в `src/models.py`):
```python
class UserAge(BaseModel):
    name: str
    age: int

class UserAgeResponse(BaseModel):
    name: str
    age: int
    is_adult: bool
```

**Примеры запросов:**
```bash
# curl
curl -X POST "http://localhost:8000/user" \
  -H "Content-Type: application/json" \
  -d '{"name":"Иван","age":25}'

# На странице тестирования:
# Введи имя "Иван" и возраст 25, нажми "Тест"
```

---

### 📌 Задание 2.1 - POST /feedback (Отправка отзыва)

**Маршрут:** `POST /feedback`

**Описание:** Принимает отзыв с именем и текстом сообщения. Сохраняет отзывы в памяти сервера.

**Входные данные** (JSON):
```json
{
  "name": "Мария",
  "message": "Отличное приложение, очень доволен работой!"
}
```

**Ответ:**
```json
{
  "message": "Спасибо, Мария! Ваш отзыв сохранён."
}
```

**Примеры запросов:**
```bash
# curl
curl -X POST "http://localhost:8000/feedback" \
  -H "Content-Type: application/json" \
  -d '{"name":"Мария","message":"Отличное приложение, очень доволен работой!"}'

# На странице тестирования:
# Введи имя "Мария" и отзыв, нажми "Отправить"
```

---

### 📌 Задание 2.2 - POST /feedback (Валидация на запретные слова)

**Описание:** Валидирует входные данные отзыва:

✅ **Правила валидации:**
- **Имя:** минимум 2 символа, максимум 50 символов
- **Сообщение:** минимум 10 символов, максимум 500 символов
- **Запретные слова:** `кринж`, `рофл`, `вайб` (в любом регистре)
- Если валидация не пройдена, вернёется HTTP 422 с описанием ошибки

**Примеры:**

✅ **Валидный запрос:**
```json
{
  "name": "Маша",
  "message": "Отличное приложение, очень доволен работой!"
}
```
→ HTTP 201 Created ✓

❌ **Невалидный запрос (имя слишком короткое):**
```json
{
  "name": "М",
  "message": "Отличное приложение!"
}
```
→ HTTP 422 Unprocessable Entity (at least 2 characters)

❌ **Невалидный запрос (запретное слово):**
```json
{
  "name": "Маша",
  "message": "Это как-то кринж выглядит честно"
}
```
→ HTTP 422 Unprocessable Entity (Слово "кринж" запрещено в отзывах)

**Валидация реализована в** `src/models.py`:
```python
class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    
    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v: str) -> str:
        forbidden_words = ['кринж', 'рофл', 'вайб']
        for word in forbidden_words:
            if word in v.lower():
                raise ValueError(f'Слово "{word}" запрещено в отзывах')
        return v
```

---

## 🧪 Подробное руководство по тестированию

### Способ 1: Интерактивная страница тестирования (РЕКОМЕНДУЕТСЯ)

1. **Откройи в браузере:** http://localhost:8000/test

2. **Видишь красивый интерфейс со всеми заданиями**

3. **Для каждого задания:**
   - 📖 Прочитай описание
   - ✏️ Заполни нужные поля (если требуются)
   - 🔘 Нажми кнопку "Тест", "Открыть" или "Отправить"
   - 📊 Посмотри результат ниже

4. **Какие кнопки нажимать:**
   - **Задание 1.1:** Нажми "Тест" - увидишь JSON ответ
   - **Задание 1.2:** Нажми "Открыть" - откроется HTML страница
   - **Задание 1.3:** Введи два числа, нажми "Тест"
   - **Задание 1.4:** Нажми "Тест" - увидишь данные пользователя
   - **Задание 1.5:** Введи имя и возраст, нажми "Тест"
   - **Задание 2.1/2.2:** Введи имя и отзыв, нажми "Отправить"

5. **Внизу страницы есть быстрые ссылки** на все основные маршруты

---

### Способ 2: Swagger документация

1. **Откройи в браузере:** http://localhost:8000/docs

2. **Видишь интерактивную документацию REST API**

3. **Для каждого endpoint'а:**
   - Нажми на название endpoint'а (GET, POST и т.д.)
   - Видишь описание и параметры
   - Нажми "Try it out"
   - Заполни параметры
   - Нажми "Execute"
   - Видишь ответ сервера

---

### Способ 3: curl команды в терминале

```bash
# Задание 1.1
curl http://localhost:8000/

# Задание 1.2
curl http://localhost:8000/html

# Задание 1.3
curl -X POST "http://localhost:8000/calculate?num1=10&num2=5.5"

# Задание 1.4
curl http://localhost:8000/users

# Задание 1.5 - тест совершеннолетния (18+)
curl -X POST http://localhost:8000/user \
  -H "Content-Type: application/json" \
  -d '{"name":"Иван","age":25}'

# Задание 1.5 - тест несовершеннолетия (<18)
curl -X POST http://localhost:8000/user \
  -H "Content-Type: application/json" \
  -d '{"name":"Петя","age":15}'

# Задание 2.1/2.2 - валидный отзыв
curl -X POST http://localhost:8000/feedback \
  -H "Content-Type: application/json" \
  -d '{"name":"Маша","message":"Отличное приложение, спасибо!"}'

# Задание 2.2 - тест на запретные слова (ОШИБКА!)
curl -X POST http://localhost:8000/feedback \
  -H "Content-Type: application/json" \
  -d '{"name":"Маша","message":"Это прям кринж какой-то"}'

# Дополнительно - просмотреть все отзывы
curl http://localhost:8000/feedbacks
```

---

## ✅ Чек-лист для проверки всех заданий

- [ ] **1.1** - GET / возвращает JSON "Авторелоад действительно работает"
- [ ] **1.2** - GET /html возвращает HTML с текстом "Я ОБОЖАЮ ВСТАВАТЬ К ПЕРВОЙ ПАРЕ :)"
- [ ] **1.3** - POST /calculate с параметрами num1, num2 возвращает их сумму
- [ ] **1.4** - GET /users возвращает User модель с name и id
- [ ] **1.5** - POST /user проверяет возраст и возвращает is_adult флаг
- [ ] **2.1** - POST /feedback принимает и сохраняет отзыв
- [ ] **2.2** - POST /feedback валидирует: имя 2-50 символов, сообщение 10-500 символов, блокирует слова "кринж", "рофл", "вайб"

---

## 🔧 Структура кода в src/app.py

В файле `src/app.py` определены все маршруты:

```python
app = FastAPI()

# Задание 1.1
@app.get("/")
def read_root():
    return {"message": "Авторелоад действительно работает"}

# Задание 1.2
@app.get("/html")
def read_html():
    return FileResponse("src/templates/index.html", media_type="text/html")

# Задание 1.3
@app.post("/calculate")
def calculate(num1: float, num2: float):
    result = num1 + num2
    return {"result": result}

# Задание 1.4
@app.get("/users")
def get_users():
    return {"name": "Дарья Невская", "id": 1}

# Задание 1.5
@app.post("/user")
def create_user(user: UserAge) -> UserAgeResponse:
    is_adult = user.age >= 18
    return UserAgeResponse(name=user.name, age=user.age, is_adult=is_adult)

# Задание 2.1 / 2.2
@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    feedbacks.append({"name": feedback.name, "message": feedback.message})
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}

# Дополнительно
@app.get("/feedbacks")
def get_all_feedbacks():
    return {"feedbacks": feedbacks, "count": len(feedbacks)}

@app.get("/test")
def get_test_page():
    return FileResponse("src/templates/test.html", media_type="text/html")
```

---

## 🔍 Структура кода в src/models.py

Все Pydantic модели для валидации:

```python
class User(BaseModel):
    name: str
    id: int

class UserAge(BaseModel):
    name: str
    age: int

class UserAgeResponse(BaseModel):
    name: str
    age: int
    is_adult: bool

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    
    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v: str) -> str:
        forbidden_words = ['кринж', 'рофл', 'вайб']
        for word in forbidden_words:
            if word in v.lower():
                raise ValueError(f'Слово "{word}" запрещено в отзывах')
        return v
```

---

## 💡 Ответ на вопрос про HTTP 422 ошибки в Swagger

**Вопрос:** Почему в Swagger документации (/docs) под endpoint'ом /calculate показана ошибка HTTP 422?

**Ответ:** ✅ **Это нормально и оставляем как есть!**

Это часть **Задания 2.2** про валидацию! FastAPI автоматически документирует:
- Что произойдёт при неправильных параметрах (num1, num2)
- Какая ошибка вернётся (HTTP 422)
- Как выглядит ошибка валидации

Это **хорошее API документирование** - показывает разработчикам, что может пойти не так и как это обработать.

**Пример:**
```bash
# Правильный запрос → HTTP 200 OK
curl -X POST "http://localhost:8000/calculate?num1=10&num2=5"

# Неправильный запрос (буква вместо числа) → HTTP 422
curl -X POST "http://localhost:8000/calculate?num1=abc&num2=5"
```

---

## 📦 Зависимости проекта

Из файла `requirements.txt`:

| Пакет | Версия | Назначение |
|-------|--------|-----------|
| **fastapi** | 0.104.1 | Веб-фреймворк для создания REST API |
| **uvicorn** | 0.24.0 | ASGI сервер для запуска приложения |
| **pydantic** | 2.5.0 | Валидация данных и типизация |
| **python-multipart** | 0.0.6 | Поддержка form-data в запросах |

---

## 🐛 Возможные проблемы и решения

### Проблема: "Address already in use: ('0.0.0.0', 8000)"

**Решение:** Порт 8000 занят другим процессом

```bash
# Убить процесс на порте 8000
lsof -ti:8000 | xargs kill -9

# Или запустить на другом порту
# Измени в main_run.py: port=8000 → port=8001
```

### Проблема: "ModuleNotFoundError: No module named 'fastapi'"

**Решение:** Установи зависимости

```bash
pip install -r requirements.txt
```

### Проблема: HTML файлы не открываются

**Решение:** Проверь, что файлы находятся в правильной папке

```bash
# Проверь структуру
ls -la src/templates/
# Должны быть: index.html, test.html
```

---

## 📚 Дополнительные ресурсы

- **FastAPI документация:** https://fastapi.tiangolo.com/
- **Pydantic документация:** https://docs.pydantic.dev/
- **Uvicorn документация:** https://www.uvicorn.org/

---

## 👨‍💻 Автор

Контрольная работа №1 по курсу "Технологии Серверных Приложений"

---

## 📄 Лицензия

MIT License - используй свободно в образовательных целях

---

## 🎉 Результат

**Все 7 заданий реализованы и протестированы!** ✅

Проект готов к сдаче с полной документацией и интерактивным интерфейсом тестирования.

Для запуска:
```bash
python3 main_run.py
# Открой http://localhost:8000/test
```
