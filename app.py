"""
app.py — Главное приложение: консольное меню демонстраций Arcade.

Запуск:
    pip install arcade
    python app.py
"""

from logic import (
    demo_primitives,
    demo_animation,
    demo_events,
    demo_sprites,
    demo_full,
)


def show_menu():
    """Выводит главное меню демонстраций."""
    print("\n")
    print("=" * 50)
    print("  🎮 ARCADE ДЕМОНСТРАЦИОННЫЙ ПРОЕКТ")
    print("=" * 50)
    print("  1. 🔷  Геометрические примитивы")
    print("  2. ⚽  Анимация — прыгающий шар")
    print("  3. 🖱️   Обработка событий (клавиши + мышь)")
    print("  4. 🟣  Спрайты и SpriteList")
    print("  5. 🚀  Полная демонстрация всех возможностей")
    print("  0. ❌  Выход")
    print("-" * 50)
    print("  Выберите пункт (0–5): ", end="")


def main():
    """Главный цикл приложения."""
    print("\n  Добро пожаловать в демонстрационный стенд Arcade!")
    print("  Каждое демо открывает отдельное графическое окно.")
    print("  Нажмите ESC или закройте окно для возврата в меню.")

    while True:
        show_menu()
        raw = input().strip()

        try:
            choice = int(raw)
        except ValueError:
            print("  ⚠️  Неверный ввод. Введите число от 0 до 5.")
            continue

        if choice == 0:
            print("\n  До свидания!\n")
            break
        elif choice == 1:
            demo_primitives()
        elif choice == 2:
            demo_animation()
        elif choice == 3:
            demo_events()
        elif choice == 4:
            demo_sprites()
        elif choice == 5:
            demo_full()
        else:
            print("  ⚠️  Выберите число от 0 до 5.")


if __name__ == "__main__":
    main()
