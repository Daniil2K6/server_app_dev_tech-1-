#!/usr/bin/env /opt/homebrew/bin/python3

"""
FAPI_KR1 - Контрольная работа №1 по FastAPI
Entry point для запуска приложения с красивым выводом.
"""

import sys
import uvicorn


def main():
    """Запуск приложения Uvicorn с красивым оформлением."""
    
    print("\n" + "="*60)
    print("🚀 FAPI_KR1 - Запуск сервера")
    print("="*60)
    print()
    print("📌 Адреса для доступа:")
    print("   • Интерактивное тестирование:")
    print("     🎯 http://localhost:8000/test")
    print()
    print("   • API Documentation:")
    print("     📚 http://localhost:8000/docs (Swagger)")
    print("     📄 http://localhost:8000/redoc (ReDoc)")
    print()
    print("   • API Endpoints:")
    print("     🏠 http://localhost:8000 (Задание 1.1)")
    print("     🌐 http://localhost:8000/html (Задание 1.2)")
    print()
    print("⏹️  Для остановки сервера нажмите: CTRL+C")
    print("="*60)
    print()
    
    # Запуск сервера
    uvicorn.run(
        "app:main_app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Сервер остановлен. До встречи! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        sys.exit(1)
