"""
logic.py — Логика демонстраций возможностей библиотеки Arcade.

Каждый класс — отдельное демонстрационное окно, наследующееся от BaseWindow.
Запуск: функции demo_*() создают окно и вызывают arcade.run().
"""

import math
import random
import arcade

from core import BaseWindow, SCREEN_WIDTH, SCREEN_HEIGHT, run_demo
from utils import random_color, color_from_angle, draw_star, print_demo_header


# ──────────────────────────────────────────────
# Демонстрация 1: Рисование примитивов
# ──────────────────────────────────────────────

class PrimitivesWindow(BaseWindow):
    """
    Демонстрирует рисование геометрических примитивов Arcade:
    линии, прямоугольники, окружности, треугольники, многоугольники, звёзды.
    """

    def __init__(self):
        super().__init__("Arcade Demo — Примитивы (ESC для выхода)")
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

    def on_draw(self):
        self.clear()

        # Линии
        for i in range(10):
            arcade.draw_line(0, i * 20, 150, i * 20 + 10,
                             color_from_angle(i * 36), 2)

        # Прямоугольники
        arcade.draw_rectangle_filled(250, 500, 120, 60, arcade.color.CORAL)
        arcade.draw_rectangle_outline(250, 500, 120, 60, arcade.color.WHITE, 3)

        # Окружности
        arcade.draw_circle_filled(450, 500, 45, arcade.color.CYAN)
        arcade.draw_circle_outline(450, 500, 45, arcade.color.WHITE, 2)

        # Эллипс
        arcade.draw_ellipse_filled(650, 500, 100, 50, arcade.color.YELLOW_GREEN)

        # Треугольник
        arcade.draw_triangle_filled(150, 350, 50, 200, 250, 200,
                                    arcade.color.LIGHT_SALMON)
        arcade.draw_triangle_outline(150, 350, 50, 200, 250, 200,
                                     arcade.color.WHITE, 2)

        # Многоугольник (шестиугольник)
        hex_pts = [(400 + 60 * math.cos(math.radians(60 * i)),
                    300 + 60 * math.sin(math.radians(60 * i)))
                   for i in range(6)]
        arcade.draw_polygon_filled(hex_pts, arcade.color.MEDIUM_PURPLE)
        arcade.draw_polygon_outline(hex_pts, arcade.color.WHITE, 2)

        # Звезда
        draw_star(650, 280, 70, 30, 5, arcade.color.GOLD)

        # Дуга
        arcade.draw_arc_outline(150, 150, 100, 100,
                                arcade.color.ORANGE, 0, 270, 4)

        # Подписи
        arcade.draw_text("Линии",        10,  190, arcade.color.WHITE, 12)
        arcade.draw_text("Прямоугольник",180, 460, arcade.color.WHITE, 12)
        arcade.draw_text("Окружность",   410, 460, arcade.color.WHITE, 12)
        arcade.draw_text("Эллипс",       600, 460, arcade.color.WHITE, 12)
        arcade.draw_text("Треугольник",   60, 185, arcade.color.WHITE, 12)
        arcade.draw_text("Шестиугольник",350, 245, arcade.color.WHITE, 12)
        arcade.draw_text("Звезда",        610, 225, arcade.color.WHITE, 12)
        arcade.draw_text("Дуга",          95, 95,  arcade.color.WHITE, 12)


def demo_primitives():
    """Запускает демонстрацию геометрических примитивов."""
    print_demo_header("ДЕМО 1: Геометрические примитивы")
    win = PrimitivesWindow()
    run_demo(win)


# ──────────────────────────────────────────────
# Демонстрация 2: Анимация
# ──────────────────────────────────────────────

class AnimationWindow(BaseWindow):
    """
    Демонстрирует анимацию: шар прыгает по экрану, меняет цвет.
    Показывает on_update(), delta_time и отражение от границ.
    """

    def __init__(self):
        super().__init__("Arcade Demo — Анимация (ESC для выхода)")
        arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
        self.x    = SCREEN_WIDTH  / 2
        self.y    = SCREEN_HEIGHT / 2
        self.vx   = 280.0
        self.vy   = 190.0
        self.r    = 30
        self.hue  = 0.0
        self.trail = []  # шлейф позиций

    def on_update(self, delta_time: float):
        self.x += self.vx * delta_time
        self.y += self.vy * delta_time

        if self.x - self.r < 0:
            self.x = self.r;          self.vx = abs(self.vx)
        if self.x + self.r > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.r;  self.vx = -abs(self.vx)
        if self.y - self.r < 0:
            self.y = self.r;          self.vy = abs(self.vy)
        if self.y + self.r > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.r;  self.vy = -abs(self.vy)

        self.hue = (self.hue + 120 * delta_time) % 360
        self.trail.append((self.x, self.y))
        if len(self.trail) > 25:
            self.trail.pop(0)

    def on_draw(self):
        self.clear()

        # Шлейф
        for i, (tx, ty) in enumerate(self.trail):
            alpha = int(255 * i / len(self.trail))
            color = color_from_angle(self.hue, 180) + (alpha,)
            arcade.draw_circle_filled(tx, ty,
                self.r * i / len(self.trail), color)

        # Шар
        color = color_from_angle(self.hue)
        arcade.draw_circle_filled(self.x, self.y, self.r, color)
        arcade.draw_circle_outline(self.x, self.y, self.r,
                                   arcade.color.WHITE, 2)
        # Блик
        arcade.draw_circle_filled(
            self.x - self.r * 0.3,
            self.y + self.r * 0.3,
            self.r * 0.25,
            (255, 255, 255, 160)
        )

        arcade.draw_text(f"Скорость: ({self.vx:.0f}, {self.vy:.0f})",
                         10, 10, arcade.color.WHITE, 14)


def demo_animation():
    """Запускает демонстрацию анимации."""
    print_demo_header("ДЕМО 2: Анимация — прыгающий шар")
    win = AnimationWindow()
    run_demo(win)


# ──────────────────────────────────────────────
# Демонстрация 3: Обработка событий
# ──────────────────────────────────────────────

class EventsWindow(BaseWindow):
    """
    Демонстрирует обработку событий: клавиатура и мышь.
    Фигура следует за мышью, клавиши меняют цвет и форму.
    """

    def __init__(self):
        super().__init__("Arcade Demo — События (ESC для выхода)")
        arcade.set_background_color((25, 25, 40))
        self.mx       = SCREEN_WIDTH  // 2
        self.my       = SCREEN_HEIGHT // 2
        self.color    = arcade.color.CYAN
        self.is_circle = True
        self.size     = 40
        self.event_count = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.mx = x
        self.my = y
        self.event_count += 1

    def on_key_press(self, key, modifiers):
        super().on_key_press(key, modifiers)
        if key == arcade.key.R:
            self.color = arcade.color.RED_ORANGE
        elif key == arcade.key.G:
            self.color = arcade.color.LIME_GREEN
        elif key == arcade.key.B:
            self.color = arcade.color.DODGER_BLUE
        elif key == arcade.key.SPACE:
            self.is_circle = not self.is_circle
        elif key == arcade.key.UP:
            self.size = min(self.size + 10, 120)
        elif key == arcade.key.DOWN:
            self.size = max(self.size - 10, 10)
        self.event_count += 1

    def on_mouse_press(self, x, y, button, modifiers):
        self.color = random_color()
        self.event_count += 1

    def on_draw(self):
        self.clear()

        # Сетка
        for x in range(0, SCREEN_WIDTH, 50):
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT, (50, 50, 70), 1)
        for y in range(0, SCREEN_HEIGHT, 50):
            arcade.draw_line(0, y, SCREEN_WIDTH, y, (50, 50, 70), 1)

        # Перекрестие курсора
        arcade.draw_line(self.mx - 20, self.my,
                         self.mx + 20, self.my, arcade.color.WHITE, 1)
        arcade.draw_line(self.mx, self.my - 20,
                         self.mx, self.my + 20, arcade.color.WHITE, 1)

        # Фигура
        if self.is_circle:
            arcade.draw_circle_filled(self.mx, self.my, self.size, self.color)
            arcade.draw_circle_outline(self.mx, self.my, self.size,
                                       arcade.color.WHITE, 2)
        else:
            arcade.draw_rectangle_filled(self.mx, self.my,
                                         self.size * 2, self.size * 2,
                                         self.color)
            arcade.draw_rectangle_outline(self.mx, self.my,
                                          self.size * 2, self.size * 2,
                                          arcade.color.WHITE, 2)

        # Подсказки
        arcade.draw_text("R/G/B — цвет  |  ПРОБЕЛ — форма  |  ↑↓ — размер  |  ЛКМ — случайный цвет",
                         10, 10, arcade.color.LIGHT_GRAY, 12)
        arcade.draw_text(f"Событий: {self.event_count}",
                         10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 14)
        arcade.draw_text(f"Форма: {'Круг' if self.is_circle else 'Квадрат'}  |  Размер: {self.size}",
                         10, SCREEN_HEIGHT - 55, arcade.color.LIGHT_GRAY, 13)


def demo_events():
    """Запускает демонстрацию обработки событий."""
    print_demo_header("ДЕМО 3: Обработка событий (клавиатура + мышь)")
    print("  R/G/B       — меняет цвет фигуры")
    print("  ПРОБЕЛ      — переключает форму (круг / квадрат)")
    print("  ↑ / ↓       — увеличивает / уменьшает размер")
    print("  ЛКМ         — случайный цвет")
    win = EventsWindow()
    run_demo(win)


# ──────────────────────────────────────────────
# Демонстрация 4: Спрайты
# ──────────────────────────────────────────────

class SpritesWindow(BaseWindow):
    """
    Демонстрирует работу со спрайтами Arcade.
    Создаёт SpriteLists с цветными кругами, управляет физикой движения.
    """

    def __init__(self):
        super().__init__("Arcade Demo — Спрайты (ESC для выхода)")
        arcade.set_background_color((15, 15, 35))
        self.balls = arcade.SpriteList()
        self.hue   = 0.0

        for i in range(15):
            ball = arcade.SpriteCircle(
                radius=random.randint(15, 35),
                color=random_color(),
                soft=True
            )
            ball.center_x = random.randint(50, SCREEN_WIDTH  - 50)
            ball.center_y = random.randint(50, SCREEN_HEIGHT - 50)
            ball.change_x = random.uniform(-200, 200)
            ball.change_y = random.uniform(-200, 200)
            self.balls.append(ball)

    def on_update(self, delta_time: float):
        self.hue = (self.hue + 60 * delta_time) % 360

        for ball in self.balls:
            ball.center_x += ball.change_x * delta_time
            ball.center_y += ball.change_y * delta_time

            if ball.left < 0:
                ball.left = 0;           ball.change_x = abs(ball.change_x)
            if ball.right > SCREEN_WIDTH:
                ball.right = SCREEN_WIDTH; ball.change_x = -abs(ball.change_x)
            if ball.bottom < 0:
                ball.bottom = 0;         ball.change_y = abs(ball.change_y)
            if ball.top > SCREEN_HEIGHT:
                ball.top = SCREEN_HEIGHT; ball.change_y = -abs(ball.change_y)

    def on_draw(self):
        self.clear()
        self.balls.draw()

        arcade.draw_text(f"Спрайтов: {len(self.balls)}",
                         10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 14)
        arcade.draw_text("Нажмите ПРОБЕЛ — добавить шар  |  ESC — выход",
                         10, 10, arcade.color.LIGHT_GRAY, 12)

    def on_key_press(self, key, modifiers):
        super().on_key_press(key, modifiers)
        if key == arcade.key.SPACE:
            ball = arcade.SpriteCircle(
                radius=random.randint(15, 35),
                color=random_color(),
                soft=True
            )
            ball.center_x = SCREEN_WIDTH  // 2
            ball.center_y = SCREEN_HEIGHT // 2
            ball.change_x = random.uniform(-250, 250)
            ball.change_y = random.uniform(-250, 250)
            self.balls.append(ball)


def demo_sprites():
    """Запускает демонстрацию спрайтов."""
    print_demo_header("ДЕМО 4: Спрайты и SpriteList")
    print("  ПРОБЕЛ — добавить новый шар")
    win = SpritesWindow()
    run_demo(win)


# ──────────────────────────────────────────────
# Демонстрация 5: Полный стенд
# ──────────────────────────────────────────────

def demo_full():
    """Запускает все демонстрации последовательно."""
    print(f"\n{'=' * 50}")
    print("  ДЕМО 5: Полная демонстрация всех возможностей")
    print(f"{'=' * 50}")
    print("  Запускаем демонстрации 1–4 последовательно...\n")

    demo_primitives()
    demo_animation()
    demo_events()
    demo_sprites()

    print(f"\n{'=' * 50}")
    print("  ✅ Полный стенд завершён.")
    print(f"{'=' * 50}")
