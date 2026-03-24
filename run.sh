#!/bin/bash
# Скрипт для запуска FAPI_KR1 приложения

echo "🚀 Запуск FastAPI приложения FAPI_KR1"
echo "======================================="
echo ""
echo "📍 Приложение будет доступно по адресам:"
echo "   • http://localhost:8000          - главная страница (JSON)"
echo "   • http://localhost:8000/html     - HTML страница"
echo "   • http://localhost:8000/users    - пользователь (JSON)"
echo "   • http://localhost:8000/docs     - интерактивная документация Swagger"
echo ""
echo "Нажмите Ctrl+C для остановки сервера"
echo "======================================="
echo ""

/opt/homebrew/bin/python3 -m uvicorn app:main_app --reload --host 127.0.0.1 --port 8000
