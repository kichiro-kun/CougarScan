# -*- coding: utf-8 -*-

"""
Сущность SourceFile - исходный файл проекта.

Представляет собой файл исходного кода, который содержит элементы кода
(функции, классы, методы и т.д.). Является контейнером для CodeElement.

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'SourceFile'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# =======================================================================================
from project_code.domain.code_element import CodeElement
from project_code.domain.enums import ElementType

from typing import Iterator, List, Optional, Set, Any, Tuple


# _______________________________________________________________________________________
class SourceFile:
    """
    Исходный файл проекта, содержащий элементы кода.

    Хранит информацию о файле:
    - path: путь к файлу
    - elements: список элементов кода внутри файла
    """

    # -----------------------------------------------------------------------------------
    def __init__(self, path: str) -> None:
        """
        Создает SourceFile с указанным путем.

        Args:
            path: Путь к исходному файлу

        Raises:
            TypeError: Если path is None
            ValueError: Если path пустая строка
        """
        self.__validate_path(path)

        self.__path: str = path
        self.__elements: List[CodeElement] = []
        self.__element_keys: Set[Tuple] = set()

    # -----------------------------------------------------------------------------------
    def get_path(self) -> str:
        """
        Возвращает путь к файлу.

        Returns:
            Путь к исходному файлу
        """
        return self.__path

    # -----------------------------------------------------------------------------------
    def get_elements(self) -> List[CodeElement]:
        """
        Возвращает копию списка элементов кода.

        Возвращается копия, чтобы защитить внутреннее состояние
        от внешних изменений.

        Returns:
            Копия списка элементов кода
        """
        return list(self.__elements)

    # -----------------------------------------------------------------------------------
    def get_element_count(self) -> int:
        """
        Возвращает количество элементов в файле.

        Returns:
            Количество элементов кода
        """
        return len(self.__elements)

    # -----------------------------------------------------------------------------------
    def add_element(self, element: CodeElement) -> None:
        """
        Добавляет элемент кода в файл.

        Args:
            element: Элемент кода для добавления

        Raises:
            TypeError: Если element is None или не является CodeElement
            ValueError: Если элемент с таким name + type уже существует (дубликат)
        """
        self.__validate_element(element)
        self.__validate_no_duplicate(element)

        self.__elements.append(element)
        self.__element_keys.add(self.__get_element_key(element))

    # -----------------------------------------------------------------------------------
    def get_element_by_name(self, name: str) -> Optional[CodeElement]:
        """
        Возвращает элемент по имени.

        Если найдено несколько элементов с одинаковым именем,
        возвращается первый найденный.

        Args:
            name: Имя элемента для поиска

        Returns:
            Найденный элемент или None, если не найден

        Raises:
            TypeError: Если name is None
            ValueError: Если name пустая строка
        """
        self.__validate_name_for_search(name)

        for element in self.__elements:
            if element.get_name() == name:
                return element

        return None

    # -----------------------------------------------------------------------------------
    def get_elements_by_type(self, element_type: ElementType) -> List[CodeElement]:
        """
        Возвращает список элементов указанного типа.

        Args:
            element_type: Тип элементов для фильтрации

        Returns:
            Список элементов указанного типа (может быть пустым)

        Raises:
            TypeError: Если element_type не является экземпляром ElementType
        """
        self.__validate_element_type_for_search(element_type)

        return [
            element for element in self.__elements
            if element.get_type() == element_type
        ]

    # -----------------------------------------------------------------------------------
    def __validate_path(self, path: str) -> None:
        """
        Валидирует путь к файлу.

        Args:
            path: Путь для валидации

        Raises:
            TypeError: Если path is None
            ValueError: Если path пустая строка
        """
        if path is None:
            raise TypeError("Source file path cannot be None")
        if not path:
            raise ValueError("Source file path cannot be empty")

    # -----------------------------------------------------------------------------------
    def __validate_element(self, element: CodeElement) -> None:
        """
        Валидирует элемент кода.

        Args:
            element: Элемент для валидации

        Raises:
            TypeError: Если element is None или не является CodeElement
        """
        if element is None:
            raise TypeError("Element cannot be None")
        if not isinstance(element, CodeElement):
            raise TypeError(
                f"Element must be an instance of CodeElement, "
                f"got {type(element).__name__}"
            )

    # -----------------------------------------------------------------------------------
    def __validate_no_duplicate(self, element: CodeElement) -> None:
        """
        Проверяет, что элемент не является дубликатом.

        Дубликат определяется по комбинации name + type.
        Локация при этом не учитывается.

        Args:
            element: Элемент для проверки

        Raises:
            ValueError: Если элемент с таким name + type уже существует
        """
        key: Tuple[Any, ...] = self.__get_element_key(element)
        if key in self.__element_keys:
            raise ValueError(
                f"Duplicate element: element with name '{element.get_name()}' "
                f"and type {element.get_type()} already exists in this file"
            )

    # -----------------------------------------------------------------------------------
    def __validate_name_for_search(self, name: str) -> None:
        """
        Валидирует имя для поиска.

        Args:
            name: Имя для валидации

        Raises:
            TypeError: Если name is None
            ValueError: Если name пустая строка
        """
        if name is None:
            raise TypeError("Element name for search cannot be None")
        if not name:
            raise ValueError("Element name for search cannot be empty")

    # -----------------------------------------------------------------------------------
    def __validate_element_type_for_search(self, element_type: ElementType) -> None:
        """
        Валидирует тип элемента для поиска.

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
    def __get_element_key(self, element: CodeElement) -> Tuple:
        """
        Возвращает ключ элемента для проверки дубликатов.

        Ключ состоит из name + type (location не учитывается).

        Args:
            element: Элемент для получения ключа

        Returns:
            Кортеж (name, element_type)
        """
        return (element.get_name(), element.get_type())

    # -----------------------------------------------------------------------------------
    def __len__(self) -> int:
        """
        Возвращает количество элементов в файле.

        Returns:
            Количество элементов кода
        """
        return len(self.__elements)

    # -----------------------------------------------------------------------------------
    def __iter__(self) -> Iterator[CodeElement]:
        """
        Возвращает итератор по элементам файла.

        Returns:
            Итератор по элементам кода
        """
        return iter(self.__elements)

    # -----------------------------------------------------------------------------------
    def __contains__(self, element: object) -> bool:
        """
        Проверяет наличие элемента в файле.

        Args:
            element: Элемент для проверки

        Returns:
            True если элемент есть в файле, False иначе
        """
        return element in self.__elements

    # -----------------------------------------------------------------------------------
    def __eq__(self, other: object) -> bool:
        """
        Проверяет равенство двух SourceFile.

        Два файла считаются равными, если совпадают их:
        - путь
        - набор элементов (порядок не важен)

        Args:
            other: Другой объект для сравнения

        Returns:
            True если объекты равны, False иначе
        """
        if not isinstance(other, SourceFile):
            return False

        return (
            self.__path == other.__path and
            set(self.__elements) == set(other.__elements)
        )

    # -----------------------------------------------------------------------------------
    def __repr__(self) -> str:
        """
        Возвращает строковое представление SourceFile.

        Returns:
            Строковое представление объекта в формате:
            SourceFile(path='...', elements_count=N)
        """
        return f"SourceFile(path='{self.__path}', elements_count={len(self.__elements)})"
