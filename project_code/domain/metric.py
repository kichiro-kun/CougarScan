# -*- coding: utf-8 -*-

"""
Сущность Metric - измеримая характеристика элемента кода.

Представляет собой результат измерения определенной метрики
(например, цикломатическая сложность, количество строк кода)
для конкретного элемента исходного кода.

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'Metric'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# =======================================================================================
from project_code.domain.code_element import CodeElement


# _______________________________________________________________________________________
class Metric:
    """
    Измеримая характеристика элемента кода.

    Хранит информацию о метрике:
    - name: название метрики (например, "Cyclomatic Complexity")
    - value: числовое значение метрики (должно быть >= 0)
    - target_element: элемент кода, к которому применяется метрика
    """

    # -----------------------------------------------------------------------------------
    def __init__(self,
                 name: str, value: float, target_element: CodeElement) -> None:
        """
        Создает Metric с указанными характеристиками.

        Args:
            name: Название метрики (идентификатор)
            value: Числовое значение метрики (должно быть >= 0)
            target_element: Элемент кода, к которому применяется метрика

        Raises:
            TypeError: Если name is None, value не является числом,
                       или target_element is None / не является CodeElement
            ValueError: Если name пустая строка или value < 0
        """
        self.__validate_name(name)
        self.__validate_value(value)
        self.__validate_target_element(target_element)

        self.__name: str = name
        self.__value: float = value
        self.__target_element: CodeElement = target_element

    # -----------------------------------------------------------------------------------
    def get_name(self) -> str:
        """
        Возвращает название метрики.

        Returns:
            Название метрики (идентификатор)
        """
        return self.__name

    # -----------------------------------------------------------------------------------
    def get_value(self) -> float:
        """
        Возвращает числовое значение метрики.

        Returns:
            Числовое значение метрики
        """
        return self.__value

    # -----------------------------------------------------------------------------------
    def get_target(self) -> CodeElement:
        """
        Возвращает целевой элемент кода.

        Returns:
            Элемент кода, к которому применяется метрика
        """
        return self.__target_element

    # -----------------------------------------------------------------------------------
    def __validate_name(self, name: str) -> None:
        """
        Валидирует название метрики.

        Args:
            name: Название для валидации

        Raises:
            TypeError: Если name is None
            ValueError: Если name пустая строка
        """
        if name is None:
            raise TypeError("Metric name cannot be None")
        if not name:
            raise ValueError("Metric name cannot be empty")

    # -----------------------------------------------------------------------------------
    def __validate_value(self, value: float) -> None:
        """
        Валидирует числовое значение метрики.

        Args:
            value: Значение для валидации

        Raises:
            TypeError: Если value is None или не является числом
            ValueError: Если value < 0
        """
        if value is None:
            raise TypeError("Metric value cannot be None")
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Metric value must be a number (int or float), "
                f"got {type(value).__name__}"
            )
        if isinstance(value, bool):
            raise TypeError(
                f"Metric value must be a number (int or float), "
                f"got {type(value).__name__}"
            )
        if value < 0:
            raise ValueError(f"Metric value must be non-negative, got {value}")

    # -----------------------------------------------------------------------------------
    def __validate_target_element(self, target_element: CodeElement) -> None:
        """
        Валидирует целевой элемент кода.

        Args:
            target_element: Элемент для валидации

        Raises:
            TypeError: Если target_element is None или не является CodeElement
        """
        if target_element is None:
            raise TypeError("Metric target element cannot be None")
        if not isinstance(target_element, CodeElement):
            raise TypeError(
                f"Metric target element must be an instance of CodeElement, "
                f"got {type(target_element).__name__}"
            )

    # -----------------------------------------------------------------------------------
    def __eq__(self, other: object) -> bool:
        """
        Проверяет равенство двух Metric.

        Две метрики считаются равными, если совпадают их:
        - название
        - значение
        - целевой элемент (используется __eq__ класса CodeElement)

        Args:
            other: Другой объект для сравнения

        Returns:
            True если объекты равны, False иначе
        """
        if not isinstance(other, Metric):
            return False

        return (
            self.__name == other.__name and
            self.__value == other.__value and
            self.__target_element == other.__target_element
        )

    # -----------------------------------------------------------------------------------
    def __hash__(self) -> int:
        """
        Возвращает хэш объекта Metric.

        Хэш основан на name, value и target_element,
        что согласовано с __eq__.

        Returns:
            Хэш-значение объекта
        """
        return hash((self.__name, self.__value, self.__target_element))

    # -----------------------------------------------------------------------------------
    def __repr__(self) -> str:
        """
        Возвращает строковое представление Metric.

        Returns:
            Строковое представление объекта в формате:
            Metric(name='...', value=..., target=CodeElement(...))
        """
        return (
            f"Metric(name='{self.__name}', "
            f"value={self.__value}, "
            f"target={self.__target_element!r})"
        )
