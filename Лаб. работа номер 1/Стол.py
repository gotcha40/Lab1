class Table:
    def __init__(self, length: float, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param length: Длина стола
        :param width: Ширина стола
        :param height: Высота стола

        Примеры:
        >>> table = Table(150.0, 75.0, 75.0)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Длина стола должна быть положительным числом")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина стола должна быть положительным числом")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота стола должна быть положительным числом")

        self.length = length
        self.width = width
        self.height = height

    def is_large_table(self) -> bool:
        """
        Проверка, является ли стол большим.

        :return: Является ли стол большим

        Примеры:
        >>> table = Table(200.0, 100.0, 75.0)
        >>> table.is_large_table()
        True
        """
        ...

    def add_tablecloth(self, cloth_size: float) -> None:
        """
        Добавление скатерти на стол.

        :param cloth_size: Размер скатерти

        :raise ValueError: Если размер скатерти меньше размеров стола
        Примеры:
        >>> table = Table(150.0, 75.0, 75.0)
        >>> table.add_tablecloth(180.0)
        """
        if not isinstance(cloth_size, (int, float)):
            raise TypeError("Размер скатерти должен быть типа int или float")
        if cloth_size < self.length or cloth_size < self.width:
            raise ValueError("Размер скатерти не может быть меньше размеров стола")
        ...
