class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f'"{self.name}" by {self.author}'

    def __repr__(self) -> str:
        return f'Book(name="{self.name}", author="{self.author}")'


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # вызовет setter pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self) -> str:
        return f'{super().__str__()}, {self.pages} pages'

    def __repr__(self) -> str:
        return f'PaperBook(name="{self.name}", author="{self.author}", pages={self.pages})'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # вызовет setter duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self) -> str:
        return f'{super().__str__()}, {self.duration} hours'

    def __repr__(self) -> str:
        return f'AudioBook(name="{self.name}", author="{self.author}", duration={self.duration})'


# Примеры использования:
try:
    paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
    print(paper_book)  # Output: "1984" by Джордж Оруэлл, 328 pages

    audio_book = AudioBook("Цветы для Элджернона", "Дэниел Киз", 11.5)
    print(audio_book)  # Output: "Цветы для Элджернона" by Дэниел Киз, 11.5 hours

except ValueError as e:
    print(e)



