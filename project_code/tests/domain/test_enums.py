# -*- coding: utf-8 -*-

"""
TestCases for project_code.domain.enums

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'TestElementType',
    'TestDependencyType'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# =======================================================================================
import unittest
from project_code.domain.enums import ElementType, DependencyType
from typing import List


# _______________________________________________________________________________________
class TestElementType(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def test_element_type_values(self) -> None:
        # Check
        self.assertEqual(first=ElementType.FILE.value, second="FILE")
        self.assertEqual(first=ElementType.CLASS.value, second="CLASS")
        self.assertEqual(first=ElementType.FUNCTION.value, second="FUNCTION")
        self.assertEqual(first=ElementType.METHOD.value, second="METHOD")
        self.assertEqual(first=ElementType.MODULE.value, second="MODULE")

    # -----------------------------------------------------------------------------------
    def test_element_type_is_iterator(self) -> None:
        # Build
        elements: List[ElementType] = list(ElementType)

        # Pre-Check
        self.assertEqual(
            first=len(elements),
            second=5
        )

        # Check
        self.assertIn(member=ElementType.FILE, container=elements)
        self.assertIn(member=ElementType.CLASS, container=elements)
        self.assertIn(member=ElementType.FUNCTION, container=elements)
        self.assertIn(member=ElementType.METHOD, container=elements)
        self.assertIn(member=ElementType.MODULE, container=elements)

    # -----------------------------------------------------------------------------------
    def test_element_type_iteration_values(self) -> None:
        # Build
        values: List[str] = [element.value for element in ElementType]

        # Pre-Check
        self.assertEqual(
            first=len(values),
            second=5
        )

        # Check
        self.assertIn(member="FILE", container=values)
        self.assertIn(member="CLASS", container=values)
        self.assertIn(member="FUNCTION", container=values)
        self.assertIn(member="METHOD", container=values)
        self.assertIn(member="MODULE", container=values)

    # -----------------------------------------------------------------------------------
    def test_element_type_iteration_names(self) -> None:
        # Build
        names: List[str] = [element.name for element in ElementType]

        # Pre-Check
        self.assertEqual(
            first=len(names),
            second=5
        )

        # Check
        self.assertIn(member="FILE", container=names)
        self.assertIn(member="CLASS", container=names)
        self.assertIn(member="FUNCTION", container=names)
        self.assertIn(member="METHOD", container=names)
        self.assertIn(member="MODULE", container=names)

    # -----------------------------------------------------------------------------------
    def test_element_type_rejects_invalid_value(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Operate & Check
            ElementType(value="INVALID_TYPE")


# _______________________________________________________________________________________
class TestDependencyType(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def test_dependency_type_values(self) -> None:
        # Check
        self.assertEqual(first=DependencyType.INHERITANCE.value, second="INHERITANCE")
        self.assertEqual(first=DependencyType.FUNCTION_CALL.value, second="FUNCTION_CALL")
        self.assertEqual(first=DependencyType.IMPORT.value, second="IMPORT")
        self.assertEqual(first=DependencyType.USAGE.value, second="USAGE")

    # -----------------------------------------------------------------------------------
    def test_dependency_type_iteration(self) -> None:
        # Build
        dependencies: List[DependencyType] = list(DependencyType)

        # Pre-Check
        self.assertEqual(
            first=len(dependencies),
            second=4
        )

        # Check
        self.assertIn(member=DependencyType.INHERITANCE, container=dependencies)
        self.assertIn(member=DependencyType.FUNCTION_CALL, container=dependencies)
        self.assertIn(member=DependencyType.IMPORT, container=dependencies)
        self.assertIn(member=DependencyType.USAGE, container=dependencies)

    # -----------------------------------------------------------------------------------
    def test_dependency_type_iteration_values(self) -> None:
        # Build
        values: List[str] = [dependency.value for dependency in DependencyType]

        # Pre-Check
        self.assertEqual(
            first=len(values),
            second=4
        )

        # Check
        self.assertIn(member="INHERITANCE", container=values)
        self.assertIn(member="FUNCTION_CALL", container=values)
        self.assertIn(member="IMPORT", container=values)
        self.assertIn(member="USAGE", container=values)

    # -----------------------------------------------------------------------------------
    def test_dependency_type_iteration_names(self) -> None:
        # Build
        names: List[str] = [dependency.name for dependency in DependencyType]

        # Pre-Check
        self.assertEqual(
            first=len(names),
            second=4
        )

        # Check
        self.assertIn(member="INHERITANCE", container=names)
        self.assertIn(member="FUNCTION_CALL", container=names)
        self.assertIn(member="IMPORT", container=names)
        self.assertIn(member="USAGE", container=names)

    # -----------------------------------------------------------------------------------
    def test_dependency_type_rejects_invalid_value(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Operate & Check
            DependencyType(value="INVALID_TYPE")


if __name__ == '__main__':
    unittest.main()
