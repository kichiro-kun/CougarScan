# -*- coding: utf-8 -*-

"""
Сущность Location - позиция элемента в исходном коде.

Описывает, где находится элемент кода в файловой системе.

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'Location'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# _______________________________________________________________________________________
class Location:
    """
    Позиция элемента в исходном коде.

    Хранит информацию о местоположении элемента:
    - file_path: путь к файлу исходного кода
    - line_number: номер строки в файле
    """

    # -----------------------------------------------------------------------------------
    def __init__(self, file_path: str, line_number: int) -> None:
        """
        Создает Location с указанной позицией.

        Args:
            file_path: Путь к файлу исходного кода
            line_number: Номер строки в файле

        Raises:
            ValueError: Если file_path пустой или line_number <= 0
        """
        self.__validate_file_path(file_path)
        self.__validate_line_number(line_number)

        self.__file_path: str = file_path
        self.__line_number: int = line_number

    # -----------------------------------------------------------------------------------
    def get_file_path(self) -> str:
        """
        Возвращает путь к файлу.

        Returns:
            Путь к файлу исходного кода
        """
        return self.__file_path

    # -----------------------------------------------------------------------------------
    def get_line_number(self) -> int:
        """
        Возвращает номер строки.

        Returns:
            Номер строки в файле
        """
        return self.__line_number

    # -----------------------------------------------------------------------------------
    def __validate_file_path(self, file_path: str) -> None:
        """
        Валидирует путь к файлу.

        Args:
            file_path: Путь к файлу для валидации

        Raises:
            ValueError: Если file_path пустой
        """
        if not file_path:
            raise ValueError("File path cannot be empty!")

    # -----------------------------------------------------------------------------------
    def __validate_line_number(self, line_number: int) -> None:
        """
        Валидирует номер строки.

        Args:
            line_number: Номер строки для валидации

        Raises:
            ValueError: Если line_number <= 0
        """
        if line_number <= 0:
            raise ValueError(f"Line number must be positive, got {line_number}!")

    # -----------------------------------------------------------------------------------
    def __eq__(self, other: object) -> bool:
        """
        Проверяет равенство двух Location.

        Args:
            other: Другой объект для сравнения

        Returns:
            True если объекты равны, False иначе
        """
        if not isinstance(other, Location):
            return False

        is_equal: bool = (
            self.__file_path == other.__file_path and
            self.__line_number == other.__line_number
        )

        return is_equal

    # -----------------------------------------------------------------------------------
    def __repr__(self) -> str:
        """
        Возвращает строковое представление Location.

        Returns:
            Строковое представление объекта
        """
        return f"Location(file_path='{self.__file_path}', line_number={self.__line_number})"
