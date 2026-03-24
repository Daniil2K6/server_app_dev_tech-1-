from pydantic import BaseModel, Field, field_validator
import re


class User(BaseModel):
    """Модель пользователя для задания 1.4"""
    name: str
    id: int


class UserAge(BaseModel):
    """Модель пользователя с возрастом для задания 1.5"""
    name: str
    age: int


class UserAgeResponse(BaseModel):
    """Ответ с информацией о том, является ли пользователь взрослым"""
    name: str
    age: int
    is_adult: bool


class Feedback(BaseModel):
    """Модель обратной связи для задания 2.1 и 2.2"""
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator('message')
    @classmethod
    def validate_message(cls, v):
        """Проверка на недопустимые слова"""
        forbidden_words = ['кринж', 'рофл', 'вайб']
        text_lower = v.lower()
        
        for word in forbidden_words:
            if word in text_lower:
                raise ValueError('Использование недопустимых слов')
        
        return v
