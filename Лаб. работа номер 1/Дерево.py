class Tree:
    def __init__(self, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param height: Высота дерева
        :param age: Возраст дерева

        Примеры:
        >>> tree = Tree(5.0, 10)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст дерева должен быть неотрицательным целым числом")

        self.height = height
        self.age = age

    def produce_oxygen(self) -> float:
        """
        Вычисление количества кислорода, производимого деревом.

        :return: Количество кислорода в литрах

        Примеры:
        >>> tree = Tree(5.0, 10)
        >>> tree.produce_oxygen()
        """
        ...

    def grow(self, years: int) -> None:
        """
        Увеличение высоты дерева на количество лет.

        :param years: Количество лет

        :raise ValueError: Если количество лет отрицательное
        Примеры:
        >>> tree = Tree(5.0, 10)
        >>> tree.grow(2)
        """
        if not isinstance(years, int) or years < 0:
            raise ValueError("Количество лет должно быть неотрицательным целым числом")
        ...
