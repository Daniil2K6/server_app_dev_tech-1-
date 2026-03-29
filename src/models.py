"""
Pydantic модели для валидации данных
Используются во всех POST/GET маршрутах для типизации и проверки входных данных
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional


class User(BaseModel):
    """
    Модель пользователя для Задания 1.4
    Содержит имя и идентификатор
    """
    name: str = Field(..., description="Имя пользователя")
    id: int = Field(..., description="Уникальный идентификатор")


class UserAge(BaseModel):
    """
    Модель для входных данных Задания 1.5
    Используется в POST /user для проверки совершеннолетия
    """
    name: str = Field(..., description="Имя пользователя")
    age: int = Field(..., description="Возраст пользователя", ge=0, le=150)


class UserAgeResponse(BaseModel):
    """
    Модель ответа для Задания 1.5
    Возвращает информацию о пользователе и статус совершеннолетия
    """
    name: str = Field(..., description="Имя пользователя")
    age: int = Field(..., description="Возраст пользователя")
    is_adult: bool = Field(..., description="Взрослый ли пользователь (age >= 18)")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Иван",
                "age": 25,
                "is_adult": True
            }
        }
    }


class Feedback(BaseModel):
    """
    Модель отзыва для Заданий 2.1 и 2.2
    Включает валидацию:
    - Имя: 2-50 символов
    - Сообщение: 10-500 символов
    - Запретные слова: кринж, рофл, вайб
    """
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Имя автора отзыва (2-50 символов)"
    )
    message: str = Field(
        ...,
        min_length=10,
        max_length=500,
        description="Текст отзыва (10-500 символов)"
    )

    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v: str) -> str:
        """
        Проверяет наличие запретных слов в сообщении
        Запретные слова: кринж, рофл, вайб
        """
        forbidden_words = ['кринж', 'рофл', 'вайб']
        message_lower = v.lower()
        
        for word in forbidden_words:
            if word in message_lower:
                raise ValueError(f'Слово "{word}" запрещено в отзывах')
        
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Мария",
                "message": "Отличное приложение, очень доволен работой!"
            }
        }
    }
