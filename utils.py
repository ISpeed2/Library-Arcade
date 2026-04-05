"""
utils.py — Вспомогательные функции: рисование фигур, цвета, таймер.

Содержит утилиты для упрощения работы с Arcade API:
генерацию цветов, рисование составных фигур и замер времени.
"""

import math
import time
import random
import arcade


def random_color() -> arcade.Color:
    """
    Генерирует случайный насыщенный цвет.

    Returns:
        Кортеж (R, G, B) с яркими значениями.
    """
    return (
        random.randint(100, 255),
        random.randint(100, 255),
        random.randint(100, 255),
    )


def color_from_angle(angle_deg: float, brightness: int = 200) -> arcade.Color:
    """
    Генерирует цвет на основе угла (имитация HSV-перехода).

    Args:
        angle_deg:  Угол в градусах (0–360).
        brightness: Яркость базовых компонент.

    Returns:
        Кортеж (R, G, B).
    """
    r = int(brightness * (0.5 + 0.5 * math.sin(math.radians(angle_deg))))
    g = int(brightness * (0.5 + 0.5 * math.sin(math.radians(angle_deg + 120))))
    b = int(brightness * (0.5 + 0.5 * math.sin(math.radians(angle_deg + 240))))
    return (r, g, b)


def draw_star(cx: float, cy: float, outer: float,
              inner: float, points: int, color: arcade.Color):
    """
    Рисует закрашенную звезду.

    Args:
        cx, cy:  Центр звезды.
        outer:   Внешний радиус.
        inner:   Внутренний радиус.
        points:  Количество лучей.
        color:   Цвет заливки.
    """
    verts = []
    for i in range(points * 2):
        angle = math.radians(i * 180 / points - 90)
        r = outer if i % 2 == 0 else inner
        verts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    arcade.draw_polygon_filled(verts, color)


def print_demo_header(name: str):
    """
    Выводит заголовок демонстрации в консоль.

    Args:
        name: Название демонстрации.
    """
    print(f"\n{'=' * 50}")
    print(f"  {name}")
    print(f"{'=' * 50}")
    print("  Закройте окно или нажмите ESC для возврата в меню.\n")


class Timer:
    """Простой таймер для замера времени."""

    def __init__(self):
        self._start = None

    def start(self):
        """Запускает таймер."""
        self._start = time.perf_counter()

    def elapsed(self) -> float:
        """Возвращает прошедшее время в секундах."""
        return time.perf_counter() - self._start
