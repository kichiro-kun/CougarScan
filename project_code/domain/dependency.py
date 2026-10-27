# -*- coding: utf-8 -*-

"""
Сущность Dependency - связь между двумя элементами кода.

Описывает направленную зависимость от одного элемента кода (source)
к другому элементу кода (target) с определенным типом связи.

Поддерживает self-reference (рекурсивные зависимости).

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'CodeElement'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# =======================================================================================
from project_code.domain.code_element import CodeElement
from project_code.domain.enums import DependencyType


# _______________________________________________________________________________________
class Dependency:
    """
    Связь между двумя элементами кода.

    Хранит информацию о зависимости:
    - source: элемент, который зависит (источник зависимости)
    - target: элемент, от которого зависят (цель зависимости)
    - dependency_type: тип зависимости (из DependencyType)

    *Разрешён self-reference (source == target) для рекурсивных зависимостей
    """

    # -----------------------------------------------------------------------------------
    def __init__(self,
                 source: CodeElement, target: CodeElement,
                 dependency_type: DependencyType) -> None:
        """
        Создает Dependency между двумя элементами кода.

        Args:
            source: Элемент-источник зависимости
            target: Элемент-цель зависимости
            dependency_type: Тип зависимости из перечисления DependencyType

        Raises:
            TypeError: Если source или target is None, не являются CodeElement,
                       или dependency_type не является DependencyType
        """
        self.__validate_source(source)
        self.__validate_target(target)
        self.__validate_dependency_type(dependency_type)

        self.__source: CodeElement = source
        self.__target: CodeElement = target
        self.__dependency_type: DependencyType = dependency_type

    # -----------------------------------------------------------------------------------
    def get_source(self) -> CodeElement:
        """
        Возвращает элемент-источник зависимости.

        Returns:
            Элемент кода, который зависит от другого элемента
        """
        return self.__source

    # -----------------------------------------------------------------------------------
    def get_target(self) -> CodeElement:
        """
        Возвращает элемент-цель зависимости.

        Returns:
            Элемент кода, от которого зависят
        """
        return self.__target

    # -----------------------------------------------------------------------------------
    def get_type(self) -> DependencyType:
        """
        Возвращает тип зависимости.

        Returns:
            Тип зависимости из перечисления DependencyType
        """
        return self.__dependency_type

    # -----------------------------------------------------------------------------------
    def __validate_source(self, source: CodeElement) -> None:
        """
        Валидирует элемент-источник зависимости.

        Args:
            source: Элемент для валидации

        Raises:
            TypeError: Если source is None или не является CodeElement
        """
        if source is None:
            raise TypeError("Dependency source cannot be None")
        if not isinstance(source, CodeElement):
            raise TypeError(
                f"Dependency source must be an instance of CodeElement, "
                f"got {type(source).__name__}"
            )

    # -----------------------------------------------------------------------------------
    def __validate_target(self, target: CodeElement) -> None:
        """
        Валидирует элемент-цель зависимости.

        Args:
            target: Элемент для валидации

        Raises:
            TypeError: Если target is None или не является CodeElement
        """
        if target is None:
            raise TypeError("Dependency target cannot be None")
        if not isinstance(target, CodeElement):
            raise TypeError(
                f"Dependency target must be an instance of CodeElement, "
                f"got {type(target).__name__}"
            )

    # -----------------------------------------------------------------------------------
    def __validate_dependency_type(self, dependency_type: DependencyType) -> None:
        """
        Валидирует тип зависимости.

        Args:
            dependency_type: Тип для валидации

        Raises:
            TypeError: Если dependency_type не является экземпляром DependencyType
        """
        if dependency_type is None:
            raise TypeError("Dependency type cannot be None")
        if not isinstance(dependency_type, DependencyType):
            raise TypeError(
                f"Dependency type must be an instance of DependencyType, "
                f"got {type(dependency_type).__name__}"
            )

    # -----------------------------------------------------------------------------------
    def __eq__(self, other: object) -> bool:
        """
        Проверяет равенство двух Dependency.

        Две зависимости считаются равными, если совпадают их:
        - source
        - target
        - dependency_type

        Args:
            other: Другой объект для сравнения

        Returns:
            True если объекты равны, False иначе
        """
        if not isinstance(other, Dependency):
            return False

        return (
            self.__source == other.__source and
            self.__target == other.__target and
            self.__dependency_type == other.__dependency_type
        )

    # -----------------------------------------------------------------------------------
    def __hash__(self) -> int:
        """
        Возвращает хэш объекта Dependency.

        Хэш основан на source, target и dependency_type,
        что согласовано с __eq__.

        Returns:
            Хэш-значение объекта
        """
        return hash(
            (
                self.__source,
                self.__target,
                self.__dependency_type
            )
        )

    # -----------------------------------------------------------------------------------
    def __repr__(self) -> str:
        """
        Возвращает строковое представление Dependency.

        Returns:
            Строковое представление объекта в формате:
            Dependency(source=CodeElement(...), target=CodeElement(...),
                       dependency_type=DependencyType.X)
        """
        return (
            f"Dependency(source={self.__source!r}, "
            f"target={self.__target!r}, "
            f"dependency_type={self.__dependency_type})"
        )
