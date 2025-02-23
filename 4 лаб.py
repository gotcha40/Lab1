class ElectronicDevice:
    """
    Базовый класс для всех электронных устройств.
    """

    def __init__(self, brand: str, model: str, power: int) -> None:
        """
        Конструктор для создания электронного устройства.

        :param brand: Производитель устройства.
        :param model: Модель устройства.
        :param power: Мощность устройства в ваттах.
        """
        self.__brand = brand  # Непубличный атрибут
        self.__model = model  # Непубличный атрибут
        self.power = power

    def __str__(self) -> str:
        """Возвращает строковое представление устройства."""
        return f"{self.__brand} {self.__model} мощность {self.power} Вт"

    def __repr__(self) -> str:
        """Возвращает представление объекта для отладки."""
        return f"ElectronicDevice(brand={self.__brand}, model={self.__model}, power={self.power})"

    def calculate_energy_consumption(self, hours: float) -> float:
        """
        Расчет потребляемой энергии.

        :param hours: Количество часов работы устройства.
        :return: Потребленная энергия в киловатт-часах (кВт·ч).
        """
        return (self.power * hours) / 1000


class Smartphone(ElectronicDevice):
    """
    Класс для смартфонов, унаследованный от электронных устройств.
    """

    def __init__(self, brand: str, model: str, power: int, has_5g: bool) -> None:
        """
        Конструктор для создания смартфона.

        :param brand: Производитель смартфона.
        :param model: Модель смартфона.
        :param power: Мощность смартфона в ваттах.
        :param has_5g: Поддерживает ли смартфон 5G.
        """
        super().__init__(brand, model, power)  # Унаследование конструктора базового класса
        self.has_5g = has_5g

    def __str__(self) -> str:
        """Возвращает строковое представление смартфона, включая поддержку 5G."""
        return f"{super().__str__()}, 5G поддержка: {'Да' if self.has_5g else 'Нет'}"

    def __repr__(self) -> str:
        """Возвращает представление объекта для отладки."""
        return f"Smartphone(brand={self._ElectronicDevice__brand}, model={self._ElectronicDevice__model}, power={self.power}, has_5g={self.has_5g})"

    def calculate_energy_consumption(self, hours: float) -> float:
        """
        Перегруженный метод для расчета потребляемой энергии с учетом режима работы.

        Если смартфон находится в режиме ожидания, мощность уменьшается вдвое.

        :param hours: Количество часов работы или ожидания смартфона.
        :return: Потребленная энергия в киловатт-часах (кВт·ч).
        """
        if self.has_5g:  # Условие для перегрузки
            effective_power = self.power  # Полная мощность при активном 5G
        else:
            effective_power = self.power / 2  # Половина мощности в режиме ожидания

        return (effective_power * hours) / 1000
