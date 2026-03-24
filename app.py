from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from models import User, UserAge, UserAgeResponse, Feedback

# Создание приложения FastAPI
main_app = FastAPI(title="FAPI_KR1", version="1.0.0")

# Хранилище для отзывов (Feedback)
feedbacks = []

# Хранилище пользователей (для примера в задании 1.4)
current_user = User(name="Дарья Невская", id=1)


# ========== Задание 1.1 ==========
@main_app.get("/")
def read_root():
    """Возвращает JSON с приветствием. Задание 1.1"""
    return {"message": "Авторелоад действительно работает"}


# ========== Задание 1.2 ==========
@main_app.get("/html")
def read_html():
    """Возвращает HTML страницу. Задание 1.2"""
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(html_path, media_type="text/html")


# ========== Задание 1.3 ==========
@main_app.post("/calculate")
def calculate(num1: float, num2: float):
    """Складывает два числа. Задание 1.3"""
    result = num1 + num2
    return {"result": result}


# ========== Задание 1.4 ==========
@main_app.get("/users")
def get_users():
    """Возвращает данные пользователя. Задание 1.4"""
    return {
        "name": current_user.name,
        "id": current_user.id
    }


# ========== Задание 1.5 ==========
@main_app.post("/user")
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
@main_app.post("/feedback")
def submit_feedback(feedback: Feedback):
    """Принимает обратную связь и сохраняет её. Задание 2.1 и 2.2"""
    feedbacks.append({
        "name": feedback.name,
        "message": feedback.message
    })
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}


# ========== Дополнительный маршрут для просмотра всех отзывов ==========
@main_app.get("/feedbacks")
def get_all_feedbacks():
    """Вспомогательный маршрут для просмотра всех сохранённых отзывов"""
    return {"feedbacks": feedbacks, "count": len(feedbacks)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(main_app, host="0.0.0.0", port=8000)
