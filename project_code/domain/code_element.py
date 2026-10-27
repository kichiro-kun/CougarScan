# -*- coding: utf-8 -*-

"""
Сущность CodeElement - базовая абстракция для элемента кода.

Представляет собой любую структурную единицу исходного кода:
функцию, класс, метод, модуль или файл.

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'CodeElement'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.2.0'


# =======================================================================================
from project_code.domain.location import Location
from project_code.domain.enums import ElementType


# _______________________________________________________________________________________
class CodeElement:
    """
    Базовая абстракция для любой структурной единицы кода.

    Хранит информацию об элементе:
    - name: имя элемента (идентификатор)
    - element_type: тип элемента (из ElementType)
    - location: позиция элемента в исходном коде
    """

    # -----------------------------------------------------------------------------------
    def __init__(self, name: str, element_type: ElementType, location: Location) -> None:
        """
        Создает CodeElement с указанными характеристиками.

        Args:
            name: Имя элемента (идентификатор)
            element_type: Тип элемента из перечисления ElementType
            location: Позиция элемента в исходном коде

        Raises:
            TypeError: Если name is None, element_type не является ElementType,
                       или location is None
            ValueError: Если name пустая строка
        """
        self.__validate_name(name)
        self.__validate_element_type(element_type)
        self.__validate_location(location)

        self.__name: str = name
        self.__element_type: ElementType = element_type
        self.__location: Location = location

    # -----------------------------------------------------------------------------------
    def get_name(self) -> str:
        """
        Возвращает имя элемента.

        Returns:
            Имя элемента (идентификатор)
        """
        return self.__name

    # -----------------------------------------------------------------------------------
    def get_type(self) -> ElementType:
        """
        Возвращает тип элемента.

        Returns:
            Тип элемента из перечисления ElementType
        """
        return self.__element_type

    # -----------------------------------------------------------------------------------
    def get_location(self) -> Location:
        """
        Возвращает локацию элемента.

        Returns:
            Позиция элемента в исходном коде
        """
        return self.__location

    # -----------------------------------------------------------------------------------
    def __validate_name(self, name: str) -> None:
        """
        Валидирует имя элемента.

        Args:
            name: Имя для валидации

        Raises:
            TypeError: Если name is None
            ValueError: Если name пустая строка
        """
        if name is None:
            raise TypeError("Element name cannot be None")
        if not name:
            raise ValueError("Element name cannot be empty")

    # -----------------------------------------------------------------------------------
    def __validate_element_type(self, element_type: ElementType) -> None:
        """
        Валидирует тип элемента.

        Args:
            element_type: Тип для валидации

        Raises:
            TypeError: Если element_type не является экземпляром ElementType
        """
        if not isinstance(element_type, ElementType):
            raise TypeError(
                f"Element type must be an instance of ElementType, "
                f"got {type(element_type).__name__}"
            )

    # -----------------------------------------------------------------------------------
    def __validate_location(self, location: Location) -> None:
        """
        Валидирует локацию элемента.

        Args:
            location: Локация для валидации

        Raises:
            TypeError: Если location is None
        """
        if location is None:
            raise TypeError("Element location cannot be None")
        if not isinstance(location, Location):
            raise TypeError(f"Element location must be {Location}!")

    # -----------------------------------------------------------------------------------
    def __eq__(self, other: object) -> bool:
        """
        Проверяет равенство двух CodeElement.

        Два элемента считаются равными, если совпадают их:
        - имя
        - тип
        - локация (используется __eq__ класса Location)

        Args:
            other: Другой объект для сравнения

        Returns:
            True если объекты равны, False иначе
        """
        if not isinstance(other, CodeElement):
            return False

        return (
            self.__name == other.__name and
            self.__element_type == other.__element_type and
            self.__location == other.__location
        )

    # -----------------------------------------------------------------------------------
    def __hash__(self) -> int:
        """
        Возвращает хэш объекта CodeElement.

        Хэш основан на name, element_type и location,
        что согласовано с __eq__.

        Returns:
            Хэш-значение объекта
        """
        return hash(
            (
                self.__name,
                self.__element_type,
                self.__location)
        )

    # -----------------------------------------------------------------------------------
    def __repr__(self) -> str:
        """
        Возвращает строковое представление CodeElement.

        Returns:
            Строковое представление объекта в формате:
            CodeElement(name='...', element_type=ElementType.X, location=Location(...))
        """
        return (
            f"CodeElement(name='{self.__name}', "
            f"element_type={self.__element_type}, "
            f"location={self.__location!r})"
        )
