# -*- coding: utf-8 -*-

"""
Перечисления для domain слоя.

Определяют допустимые типы элементов кода и типы зависимостей между ними.
Используются для строгой типизации и валидации на уровне бизнес-логики.

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'ElementType',
    'DependencyType'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# =======================================================================================
from enum import Enum


# _______________________________________________________________________________________
class ElementType(str, Enum):
    """
    Типы структурных элементов кода.

    Определяет, какую роль играет элемент в исходном коде:
    - FILE: файл исходного кода
    - CLASS: класс
    - FUNCTION: функция (не входящая в класс)
    - METHOD: метод класса
    - MODULE: модуль/пакет
    """
    FILE = "FILE"
    CLASS = "CLASS"
    FUNCTION = "FUNCTION"
    METHOD = "METHOD"
    MODULE = "MODULE"


# _______________________________________________________________________________________
class DependencyType(str, Enum):
    """
    Типы связей между элементами кода.

    Определяет характер зависимости между двумя элементами:
    - INHERITANCE: наследование классов
    - FUNCTION_CALL: вызов функции или метода
    - IMPORT: импорт модуля или класса
    - USAGE: общее использование (например, создание экземпляра)
    """
    INHERITANCE = "INHERITANCE"
    FUNCTION_CALL = "FUNCTION_CALL"
    IMPORT = "IMPORT"
    USAGE = "USAGE"
