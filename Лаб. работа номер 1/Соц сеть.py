class SocialNetwork:
    def __init__(self, name: str, users_count: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"

        :param name: Название социальной сети
        :param users_count: Количество пользователей

        Примеры:
        >>> network = SocialNetwork("Facebook", 3000000000)  # инициализация экземпляра класса
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Название социальной сети должно быть непустой строкой")
        if not isinstance(users_count, int) or users_count < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным целым числом")

        self.name = name
        self.users_count = users_count

    def add_user(self) -> None:
        """

            Добавление нового пользователя в сеть.

            Примеры:
            >>> network = SocialNetwork("Facebook", 3000000000)
            >>> network.add_user()
            """
        ...

    def get_active_users(self) -> int:
        """
        Получение количества активных пользователей.

        :return: Количество активных пользователей

        Примеры:
        >>> network = SocialNetwork("Facebook", 3000000000)
        >>> network.get_active_users()
        """
        ...