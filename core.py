"""
core.py — Ядро системы: базовые классы окон на основе arcade.Window.

Содержит класс BaseWindow — основу для всех демонстрационных окон.
Каждое демо наследуется от BaseWindow и переопределяет нужные методы.
"""

import arcade

# Размеры окна по умолчанию
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600


class BaseWindow(arcade.Window):
    """
    Базовый класс демонстрационного окна.

    Наследуется от arcade.Window и предоставляет общую логику:
    закрытие по ESC, отображение подсказки в заголовке окна.

    Подклассы переопределяют on_draw(), on_update(), on_key_press()
    для реализации конкретной демонстрации.
    """

    def __init__(self, title: str = "Arcade Demo",
                 width: int = SCREEN_WIDTH,
                 height: int = SCREEN_HEIGHT):
        """
        Инициализирует окно Arcade.

        Args:
            title:  Заголовок окна.
            width:  Ширина в пикселях.
            height: Высота в пикселях.
        """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def on_key_press(self, key, modifiers):
        """Закрывает окно по нажатию ESC."""
        if key == arcade.key.ESCAPE:
            self.close()

    def run(self):
        """Запускает игровой цикл окна."""
        arcade.run()


def run_demo(window: BaseWindow):
    """
    Запускает демонстрационное окно и блокирует до его закрытия.

    Args:
        window: Экземпляр демонстрационного окна.
    """
    window.run()
