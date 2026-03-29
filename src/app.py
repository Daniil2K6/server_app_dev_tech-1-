"""
FAPI_KR1 - Контрольная работа №1 по FastAPI
Основной файл приложения с определением всех маршрутов

Структура:
  src/
  ├── app.py           (этот файл - инициализация FastAPI)
  ├── models.py        (Pydantic модели для валидации)
  └── templates/       (HTML файлы)
      ├── index.html   (Задание 1.2)
      └── test.html    (Интерактивное тестирование)
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from .models import User, UserAge, UserAgeResponse, Feedback

# Создание приложения FastAPI
app = FastAPI(
    title="FAPI_KR1",
    version="1.0.0",
    description="Решение контрольной работы №1 по FastAPI",
    servers=[{"url": "http://localhost:8000", "description": "Development server"}]
)

# Хранилище для отзывов (Feedback)
feedbacks = []

# Хранилище пользователей (для примера в задании 1.4)
current_user = User(name="Дарья Невская", id=1)

# Получаем путь к папке с шаблонами
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, "src", "templates")


# ========== Задание 1.1 ==========
@app.get(
    "/",
    tags=["Задание 1.1"],
    summary="Приветствие",
    description="Возвращает JSON с приветствием. Поддерживает авторелоад при изменении кода."
)
def read_root():
    """Возвращает JSON с приветствием. Задание 1.1"""
    return {"message": "Авторелоад действительно работает"}


# ========== Задание 1.2 ==========
@app.get(
    "/html",
    tags=["Задание 1.2"],
    summary="HTML страница",
    description="Возвращает HTML страницу с текстом"
)
def read_html():
    """Возвращает HTML страницу. Задание 1.2"""
    html_path = os.path.join(TEMPLATES_DIR, "index.html")
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content=content)


# ========== Задание 1.3 ==========
@app.post(
    "/calculate",
    tags=["Задание 1.3"],
    summary="Сумма двух чисел",
    description="Складывает два числа и возвращает результат"
)
def calculate(num1: float, num2: float):
    """Складывает два числа. Задание 1.3"""
    result = num1 + num2
    return {"result": result}


# ========== Задание 1.4 ==========
@app.get(
    "/users",
    tags=["Задание 1.4"],
    summary="Получить пользователя",
    description="Возвращает данные пользователя используя Pydantic модель"
)
def get_users():
    """Возвращает данные пользователя. Задание 1.4"""
    return {
        "name": current_user.name,
        "id": current_user.id
    }


# ========== Задание 1.5 ==========
@app.post(
    "/user",
    tags=["Задание 1.5"],
    summary="Проверка совершеннолетия",
    description="Проверяет возраст пользователя и возвращает is_adult"
)
def create_user(user: UserAge) -> UserAgeResponse:
    """
    Принимает данные пользователя и определяет, взрослый ли он. Задание 1.5
    """
    is_adult = user.age >= 18
    return UserAgeResponse(
        name=user.name,
        age=user.age,
        is_adult=is_adult
    )


# ========== Задание 2.1 ==========
@app.post(
    "/feedback",
    tags=["Задание 2.1-2.2"],
    summary="Отправить отзыв",
    description="Отправляет отзыв с валидацией. Имя: 2-50 символов, текст: 10-500 символов. Запретные слова: кринж, рофл, вайб."
)
def submit_feedback(feedback: Feedback):
    """Принимает обратную связь и сохраняет её. Задание 2.1 и 2.2"""
    feedbacks.append({
        "name": feedback.name,
        "message": feedback.message
    })
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}


# ========== Дополнительные маршруты ==========
@app.get(
    "/feedbacks",
    tags=["Дополнительно"],
    summary="Получить все отзывы",
    description="Вспомогательный маршрут для просмотра всех сохранённых отзывов"
)
def get_all_feedbacks():
    """Вспомогательный маршрут для просмотра всех сохранённых отзывов"""
    return {"feedbacks": feedbacks, "count": len(feedbacks)}


@app.get(
    "/test",
    tags=["Тестирование"],
    summary="Интерактивная страница тестирования",
    description="Красивый интерфейс для тестирования всех маршрутов"
)
def get_test_page():
    """Интерактивная страница для тестирования всех маршрутов"""
    test_path = os.path.join(TEMPLATES_DIR, "test.html")
    return FileResponse(test_path, media_type="text/html")
