#!/usr/bin/env /opt/homebrew/bin/python3

import sys
import os

# Добавляем текущую папку в path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    import uvicorn
    print("=" * 60)
    print("🚀 ЗАПУСК FAPI_KR1 ПРИЛОЖЕНИЯ")
    print("=" * 60)
    print("\n📱 Откройте в браузере:")
    print("   http://localhost:8000          - главная (JSON)")
    print("   http://localhost:8000/html     - HTML страница")
    print("   http://localhost:8000/users    - пользователь")
    print("   http://localhost:8000/docs     - Swagger документация")
    print("\n📝 Нажмите Ctrl+C для остановки сервера\n")
    print("=" * 60 + "\n")
    
    uvicorn.run(
        "app:main_app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
