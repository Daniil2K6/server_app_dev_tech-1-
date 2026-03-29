#!/usr/bin/env python3
"""
Точка входа для запуска FAPI_KR1 приложения

Запуск:
    python3 main_run.py
    
Сервер запустится по адресу: http://localhost:8000
"""

import uvicorn
import os
import sys

# Добавляем текущую директорию в путь Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Запускаем FastAPI приложение
    # --reload для автоперезагрузки при изменении кода (для разработки)
    uvicorn.run(
        "src.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
