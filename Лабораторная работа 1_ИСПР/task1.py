# TODO Написать 3 класса с документацией и аннотацией типов

class Shape:
    """
    Абстрактный класс, представляющий геометрическую фигуру.
    """

    def __init__(self, color: str, is_visible: bool):
        """
        Инициализирует объект "Фигура".

        Args:
            color (str): Цвет фигуры.
            is_visible (bool): Видимость фигуры.

        Raises:
            ValueError: Если цвет пустой или не строка.
        """
        if not isinstance(color, str) or not color:
            raise ValueError("Цвет должен быть непустой строкой.")
        self.color = color
        self.is_visible = is_visible

    def color(self, value: str) -> None:
        """
        Устанавливает цвет фигуры.

        Args:
            value (str): Новый цвет.

        Raises:
            ValueError: Если цвет пустой или не строка.
        """
        if not isinstance(value, str) or not value:
            raise ValueError("Цвет должен быть непустой строкой.")
        self.color = value

    def calculate_area(self) -> float:
        """
        Абстрактный метод для вычисления площади фигуры.

        Returns:
            float: Площадь фигуры.
        """
        ...

    def move(self, dx: float, dy: float) -> None:
        """
        Абстрактный метод для перемещения фигуры.

        Args:
            dx (float): Смещение по оси X.
            dy (float): Смещение по оси Y.
        """
        ...


class Tree:
    """
    Абстрактный класс, описывающий дерево.
    """

    def __init__(self, species: str, height: float, age: int):
        """
        Инициализирует объект Tree.

        Args:
            species (str): Вид дерева (название).
            height (float): Высота дерева в метрах.
            age (int): Возраст дерева в годах.

        Raises:
            ValueError: Если высота или возраст имеют недопустимые значения.
        """
        if not isinstance(species, str) or not species:
            raise ValueError("Вид дерева должен быть непустой строкой.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст дерева должен быть неотрицательным целым числом.")

        self.species = species
        self.height = height
        self.age = age

    def grow(self, years: int) -> None:
        """
        Абстрактный метод, моделирующий рост дерева за указанное количество лет.

        Args:
            years (int): Количество лет роста.

        Raises:
            ValueError: Если количество лет меньше нуля.
        """
        ...

    def shed_leaves(self, season: str) -> None:
        """
        Абстрактный метод, моделирующий сброс листьев деревом в указанный сезон.

        Args:
            season (str): Сезон (например, "осень").

        Raises:
            ValueError: Если сезон не является строкой.
        """
        ...


class Computer:
    """
    Абстрактный класс, описывающий компьютер.
    """

    def __init__(self, os: str, ram_gb: int, cpu_model: str):
        """
        Инициализирует объект Computer.

        Args:
            os (str): Операционная система компьютера.
            ram_gb (int): Объем оперативной памяти в гигабайтах.
            cpu_model (str): Модель процессора.

        Raises:
            ValueError: Если объем оперативной памяти не является положительным целым числом, или модель процессора не является непустой строкой.
        """
        if not isinstance(ram_gb, int) or ram_gb <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным целым числом.")
        if not isinstance(cpu_model, str) or not cpu_model:
            raise ValueError("Модель процессора должна быть непустой строкой.")

        self.os = os
        self.ram_gb = ram_gb
        self.cpu_model = cpu_model

    def ram_gb(self) -> int:
        """
        Возвращает объем оперативной памяти в гигабайтах.
        """
        return self.ram_gb

    def power_on(self) -> None:
        """
        Абстрактный метод, имитирующий включение компьютера.
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest

    doctest.testmod()
