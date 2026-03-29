"""
FAPI_KR1 - Контрольная работа №1 по FastAPI
Решение 7 заданий на использование FastAPI, Pydantic и валидации
"""

from .app import app
from .models import User, UserAge, UserAgeResponse, Feedback

__all__ = [
    'app',
    'User',
    'UserAge',
    'UserAgeResponse',
    'Feedback'
]
