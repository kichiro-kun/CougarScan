# -*- coding: utf-8 -*-

"""
TestCases for project_code.domain.code_element

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'TestCodeElementCreation',
    'TestCodeElementGetters',
    'TestCodeElementEquality',
    'TestCodeElementRepr'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# =======================================================================================
import unittest

from project_code.domain.code_element import CodeElement
from project_code.domain.location import Location
from project_code.domain.enums import ElementType

from typing import Any, Tuple


# _______________________________________________________________________________________
class TestCodeElementCreation(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.location = Location(file_path="/path/to/file.py", line_number=10)
        self.valid_name = "my_function"
        self.valid_type: ElementType = ElementType.FUNCTION

    # -----------------------------------------------------------------------------------
    def test_code_element_creation_with_valid_data(self) -> None:
        # Operate
        element = CodeElement(
            name=self.valid_name,
            element_type=self.valid_type,
            location=self.location
        )

        # Check
        self.assertEqual(first=element.get_name(), second=self.valid_name)
        self.assertEqual(first=element.get_type(), second=self.valid_type)
        self.assertEqual(first=element.get_location(), second=self.location)

    # -----------------------------------------------------------------------------------
    def test_code_element_creation_with_empty_name_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Operate & Check
            CodeElement(
                name="",
                element_type=self.valid_type,
                location=self.location
            )

    # -----------------------------------------------------------------------------------
    def test_code_element_creation_with_none_name_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            CodeElement(
                name=None,  # type: ignore
                element_type=self.valid_type,
                location=self.location
            )

    # -----------------------------------------------------------------------------------
    def test_code_element_creation_with_invalid_type_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            CodeElement(
                name=self.valid_name,
                element_type="invalid_type",  # type: ignore
                location=self.location
            )

    # -----------------------------------------------------------------------------------
    def test_code_element_creation_with_none_type_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            CodeElement(
                name=self.valid_name,
                element_type=None,  # type: ignore
                location=self.location
            )

    # -----------------------------------------------------------------------------------
    def test_code_element_creation_with_none_location_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            CodeElement(
                name=self.valid_name,
                element_type=self.valid_type,
                location=None  # type: ignore
            )

    # -----------------------------------------------------------------------------------
    def test_code_element_creation_with_non_location_type_raises_error(self) -> None:
        # Build
        non_location = "non location"

        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Check & Operate
            CodeElement(
                name=self.valid_name,
                element_type=self.valid_type,
                location=non_location  # type: ignore
            )

    # -----------------------------------------------------------------------------------
    def test_code_element_creation_with_all_element_types(self) -> None:
        # Build
        assert_count: int = 0

        for element_type in ElementType:
            assert_count += 1
            # Prepare check context
            with self.subTest(msg=f"Assert №{assert_count}: *{element_type}*"):
                # Operate
                element = CodeElement(
                    name=f"element_{element_type.value}",
                    element_type=element_type,
                    location=self.location
                )

                # Check
                self.assertEqual(first=element.get_type(), second=element_type)


# _______________________________________________________________________________________
class TestCodeElementGetters(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.location = Location(file_path="/path/to/file.py", line_number=10)
        self.element = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=self.location
        )

    # -----------------------------------------------------------------------------------
    def test_get_name_returns_correct_value(self) -> None:
        # Check
        self.assertEqual(first=self.element.get_name(), second="my_function")

    # -----------------------------------------------------------------------------------
    def test_get_type_returns_correct_value(self) -> None:
        # Check
        self.assertEqual(first=self.element.get_type(), second=ElementType.FUNCTION)

    # -----------------------------------------------------------------------------------
    def test_get_location_returns_correct_value(self) -> None:
        # Check
        self.assertEqual(first=self.element.get_location(), second=self.location)

    # -----------------------------------------------------------------------------------
    def test_get_location_returns_same_object(self) -> None:
        # Build
        returned_location: Location = self.element.get_location()

        # Check
        self.assertIs(expr1=returned_location, expr2=self.location)


# _______________________________________________________________________________________
class TestCodeElementEquality(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.location = Location(file_path="/path/to/file.py", line_number=10)

    # -----------------------------------------------------------------------------------
    def test_code_element_equality_with_same_data(self) -> None:
        # Build
        element1 = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=self.location
        )
        element2 = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=self.location
        )

        # Check
        self.assertEqual(first=element1, second=element2)

    # -----------------------------------------------------------------------------------
    def test_code_element_equality_with_equal_locations(self) -> None:
        # Build
        location1 = Location(file_path="/path/to/file.py", line_number=10)
        location2 = Location(file_path="/path/to/file.py", line_number=10)

        element1 = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=location1
        )
        element2 = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=location2
        )

        # Check
        self.assertEqual(first=element1, second=element2)

    # -----------------------------------------------------------------------------------
    def test_code_element_inequality_different_name(self) -> None:
        # Build
        element1 = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=self.location
        )
        element2 = CodeElement(
            name="function2",
            element_type=ElementType.FUNCTION,
            location=self.location
        )

        # Check
        self.assertNotEqual(first=element1, second=element2)

    # -----------------------------------------------------------------------------------
    def test_code_element_inequality_different_type(self) -> None:
        # Build
        element1 = CodeElement(
            name="my_element",
            element_type=ElementType.FUNCTION,
            location=self.location
        )
        element2 = CodeElement(
            name="my_element",
            element_type=ElementType.CLASS,
            location=self.location
        )

        # Check
        self.assertNotEqual(first=element1, second=element2)

    # -----------------------------------------------------------------------------------
    def test_code_element_inequality_different_location(self) -> None:
        # Build
        location1 = Location(file_path="/path/to/file1.py", line_number=10)
        location2 = Location(file_path="/path/to/file2.py", line_number=10)

        element1 = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=location1
        )
        element2 = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=location2
        )

        # Check
        self.assertNotEqual(first=element1, second=element2)

    # -----------------------------------------------------------------------------------
    def test_code_element_inequality_with_non_code_element_object(self) -> None:
        # Build
        non_code_elements: Tuple[Any, ...] = (
            "not a code element", None, 42, {'name': "my_function"}
        )

        element = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=self.location
        )

        # Prepare check context
        assert_count: int = 0
        for non_code_element in non_code_elements:
            assert_count += 1
            with self.subTest(msg=f"Assert №{assert_count}: *{non_code_element}*"):
                # Check
                self.assertNotEqual(first=element, second=non_code_element)


# _______________________________________________________________________________________
class TestCodeElementRepr(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.location = Location(file_path="/path/to/file.py", line_number=10)
        self.element = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=self.location
        )

    # -----------------------------------------------------------------------------------
    def test_code_element_repr_contains_essential_info(self) -> None:
        # Extract
        repr_string: str = repr(self.element)

        # Check
        self.assertIn(member="CodeElement", container=repr_string)
        self.assertIn(member="my_function", container=repr_string)
        self.assertIn(member="FUNCTION", container=repr_string)
        self.assertIn(member="/path/to/file.py", container=repr_string)

    # -----------------------------------------------------------------------------------
    def test_code_element_repr_format(self) -> None:
        # Build
        expected = "CodeElement(name='my_function', element_type=ElementType.FUNCTION, location=Location(file_path='/path/to/file.py', line_number=10))"

        # Check
        self.assertEqual(first=repr(self.element), second=expected)


if __name__ == '__main__':
    unittest.main()
