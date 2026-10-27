# -*- coding: utf-8 -*-

"""
TestCases for project_code.domain.source_file

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'TestSourceFileCreation',
    'TestSourceFileGetters',
    'TestSourceFileAddElement',
    'TestSourceFileDuplicateProtection',
    'TestSourceFileSearch',
    'TestSourceFileIteration',
    'TestSourceFileEquality',
    'TestSourceFileRepr'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# =======================================================================================
import unittest

from project_code.domain.source_file import SourceFile
from project_code.domain.code_element import CodeElement
from project_code.domain.location import Location
from project_code.domain.enums import ElementType

from typing import Any, List


# _______________________________________________________________________________________
class TestSourceFileCreation(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.valid_path = "/path/to/file.py"

    # -----------------------------------------------------------------------------------
    def test_source_file_creation_with_valid_path(self) -> None:
        # Build
        source_file = SourceFile(path=self.valid_path)

        # Check
        self.assertEqual(first=source_file.get_path(), second=self.valid_path)
        self.assertEqual(first=len(source_file.get_elements()), second=0)

    # -----------------------------------------------------------------------------------
    def test_source_file_creation_with_empty_path_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Operate
            SourceFile(path="")

    # -----------------------------------------------------------------------------------
    def test_source_file_creation_with_none_path_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate
            SourceFile(path=None)  # type: ignore

    # -----------------------------------------------------------------------------------
    def test_source_file_creation_with_various_paths(self) -> None:
        # Build
        paths: List[str] = [
            "/absolute/path.py",
            "relative/path.py",
            "./current/path.py",
            "../parent/path.py",
            "file.py"
        ]

        # Prepare check context
        assert_count: int = 0
        for path in paths:
            assert_count += 1
            with self.subTest(msg=f"Assert №{assert_count}: *{path}*"):
                # Operate
                source_file = SourceFile(path=path)

                # Check
                self.assertEqual(first=source_file.get_path(), second=path)


# _______________________________________________________________________________________
class TestSourceFileGetters(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.source_file = SourceFile(path="/path/to/file.py")

        self.element1 = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        self.element2 = CodeElement(
            name="function2",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )

    # -----------------------------------------------------------------------------------
    def test_get_path_returns_correct_value(self) -> None:
        # Operate & Check
        self.assertEqual(first=self.source_file.get_path(), second="/path/to/file.py")

    # -----------------------------------------------------------------------------------
    def test_get_elements_returns_empty_list_initially(self) -> None:
        # Operate
        elements: List[Any] = self.source_file.get_elements()

        # Check
        self.assertEqual(first=len(elements), second=0)
        self.assertIsInstance(obj=elements, cls=list)

    # -----------------------------------------------------------------------------------
    def test_get_elements_returns_copy(self) -> None:
        # Build
        self.source_file.add_element(element=self.element1)

        # Operate & Extract
        elements1: List[Any] = self.source_file.get_elements()
        elements2: List[Any] = self.source_file.get_elements()

        # Check
        self.assertEqual(first=elements1, second=elements2)
        self.assertIsNot(expr1=elements1, expr2=elements2)

    # -----------------------------------------------------------------------------------
    def test_get_elements_returns_correct_elements(self) -> None:
        # Build
        self.source_file.add_element(element=self.element1)
        self.source_file.add_element(element=self.element2)

        # Operate & Extract
        elements: List[Any] = self.source_file.get_elements()

        # Check
        self.assertEqual(first=len(elements), second=2)
        self.assertIn(member=self.element1, container=elements)
        self.assertIn(member=self.element2, container=elements)

    # -----------------------------------------------------------------------------------
    def test_get_element_count_returns_correct_value(self) -> None:
        #  Check
        self.assertEqual(first=self.source_file.get_element_count(), second=0)

        # Operate
        self.source_file.add_element(self.element1)

        # Check
        self.assertEqual(first=self.source_file.get_element_count(), second=1)

        # Operate
        self.source_file.add_element(element=self.element2)

        # Check
        self.assertEqual(first=self.source_file.get_element_count(), second=2)


# _______________________________________________________________________________________
class TestSourceFileAddElement(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.source_file = SourceFile(path="/path/to/file.py")

        self.valid_element = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )

    # -----------------------------------------------------------------------------------
    def test_add_element_to_source_file(self) -> None:
        # Operate
        self.source_file.add_element(element=self.valid_element)

        # Extract
        elements: List[Any] = self.source_file.get_elements()

        # Check
        self.assertEqual(first=len(elements), second=1)
        self.assertEqual(first=elements[0], second=self.valid_element)

    # -----------------------------------------------------------------------------------
    def test_add_multiple_elements_to_source_file(self) -> None:
        # Build
        element1 = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        element2 = CodeElement(
            name="function2",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )
        element3 = CodeElement(
            name="MyClass",
            element_type=ElementType.CLASS,
            location=Location(file_path="/path/to/file.py", line_number=30)
        )

        # Operate
        self.source_file.add_element(element=element1)
        self.source_file.add_element(element=element2)
        self.source_file.add_element(element=element3)

        # Extract
        elements: List[Any] = self.source_file.get_elements()

        # Check
        self.assertEqual(first=len(elements), second=3)
        self.assertIn(member=element1, container=elements)
        self.assertIn(member=element2, container=elements)
        self.assertIn(member=element3, container=elements)

    # -----------------------------------------------------------------------------------
    def test_add_none_element_raises_error(self) -> None:
        # Preapre check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            self.source_file.add_element(element=None)  # type: ignore

    # -----------------------------------------------------------------------------------
    def test_add_non_code_element_raises_error(self) -> None:
        # Preapre check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            self.source_file.add_element(element="not a code element")  # type: ignore

        # Preapre check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            self.source_file.add_element(element={"name": "function1"})  # type: ignore

        # Preapre check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            self.source_file.add_element(element=42)  # type: ignore


# _______________________________________________________________________________________
class TestSourceFileDuplicateProtection(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.source_file = SourceFile(path="/path/to/file.py")

        self.element1 = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )

    # -----------------------------------------------------------------------------------
    def test_add_duplicate_element_raises_error(self) -> None:
        # Build
        self.source_file.add_element(element=self.element1)

        duplicate_element = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )

        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Operate & Check
            self.source_file.add_element(element=duplicate_element)

    # -----------------------------------------------------------------------------------
    def test_add_element_with_same_name_and_type_different_location_raises_error(self) -> None:
        # Build
        self.source_file.add_element(element=self.element1)

        duplicate_element = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=999)
        )

        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Operate & Check
            self.source_file.add_element(element=duplicate_element)

    # -----------------------------------------------------------------------------------
    def test_add_element_with_same_name_different_type_allowed(self) -> None:
        # Build
        function_element = CodeElement(
            name="my_element",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        class_element = CodeElement(
            name="my_element",
            element_type=ElementType.CLASS,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )

        # Operate
        self.source_file.add_element(element=function_element)
        self.source_file.add_element(element=class_element)

        # Check
        self.assertEqual(first=self.source_file.get_element_count(), second=2)

    # -----------------------------------------------------------------------------------
    def test_add_element_with_different_name_same_type_allowed(self) -> None:
        # Build
        element1 = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        element2 = CodeElement(
            name="function2",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )

        # Operate
        self.source_file.add_element(element=element1)
        self.source_file.add_element(element=element2)

        # Check
        self.assertEqual(first=self.source_file.get_element_count(), second=2)


# _______________________________________________________________________________________
class TestSourceFileSearch(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.source_file: SourceFile = SourceFile(path="/path/to/file.py")

        self.element1: CodeElement = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(
                file_path="/path/to/file.py",
                line_number=10
            )
        )
        self.element2: CodeElement = CodeElement(
            name="MyClass",
            element_type=ElementType.CLASS,
            location=Location(
                file_path="/path/to/file.py",
                line_number=20
            )
        )
        self.element3: CodeElement = CodeElement(
            name="function2",
            element_type=ElementType.FUNCTION,
            location=Location(
                file_path="/path/to/file.py",
                line_number=30
            )
        )

        self.source_file.add_element(element=self.element1)
        self.source_file.add_element(element=self.element2)
        self.source_file.add_element(element=self.element3)

    # -----------------------------------------------------------------------------------
    def test_get_element_by_name_returns_correct_element(self) -> None:
        # Operate
        found: CodeElement = self.source_file.get_element_by_name(name="function1")  # type: ignore

        # Check
        self.assertEqual(first=found, second=self.element1)

        # Operate
        found = self.source_file.get_element_by_name(name="MyClass")  # type: ignore

        # Check
        self.assertEqual(first=found, second=self.element2)

    # -----------------------------------------------------------------------------------
    def test_get_element_by_name_not_found_returns_none(self) -> None:
        # Operate
        found: Any = self.source_file.get_element_by_name(name="nonexistent")

        # Check
        self.assertIsNone(obj=found)

    # -----------------------------------------------------------------------------------
    def test_get_element_by_name_with_empty_name_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Operate & Check
            self.source_file.get_element_by_name(name="")

    # -----------------------------------------------------------------------------------
    def test_get_element_by_name_with_none_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            self.source_file.get_element_by_name(name=None)  # type: ignore

    # -----------------------------------------------------------------------------------
    def test_get_elements_by_type_returns_correct_elements(self) -> None:
        # Operate
        functions: List[CodeElement] = self.source_file.get_elements_by_type(
            element_type=ElementType.FUNCTION
        )

        # Check
        self.assertEqual(first=len(functions), second=2)
        self.assertIn(member=self.element1, container=functions)
        self.assertIn(member=self.element3, container=functions)

    # -----------------------------------------------------------------------------------
    def test_get_elements_by_type_returns_empty_list_if_not_found(self) -> None:
        # Operate
        modules: List[CodeElement] = self.source_file.get_elements_by_type(
            element_type=ElementType.MODULE
        )

        # Check
        self.assertEqual(first=len(modules), second=0)
        self.assertIsInstance(obj=modules, cls=list)

    # -----------------------------------------------------------------------------------
    def test_get_elements_by_type_with_invalid_type_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            self.source_file.get_elements_by_type(element_type="invalid_type")  # type: ignore

        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            self.source_file.get_elements_by_type(element_type=None)  # type: ignore


# _______________________________________________________________________________________
class TestSourceFileIteration(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.source_file: SourceFile = SourceFile(path="/path/to/file.py")

        self.element1: CodeElement = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(
                file_path="/path/to/file.py",
                line_number=10
            )
        )
        self.element2: CodeElement = CodeElement(
            name="function2",
            element_type=ElementType.FUNCTION,
            location=Location(
                file_path="/path/to/file.py",
                line_number=20
            )
        )

    # -----------------------------------------------------------------------------------
    def test_len_returns_correct_count(self) -> None:
        # Check
        self.assertEqual(first=len(self.source_file), second=0)

        # Operate
        self.source_file.add_element(element=self.element1)

        # Check
        self.assertEqual(first=len(self.source_file), second=1)

        # Operate
        self.source_file.add_element(element=self.element2)

        # Check
        self.assertEqual(first=len(self.source_file), second=2)

    # -----------------------------------------------------------------------------------
    def test_iteration_over_elements(self) -> None:
        # Build
        self.source_file.add_element(element=self.element1)
        self.source_file.add_element(element=self.element2)

        # Operate
        iterated_elements: List[CodeElement] = list(self.source_file)

        # Check
        self.assertEqual(first=len(iterated_elements), second=2)
        self.assertIn(member=self.element1, container=iterated_elements)
        self.assertIn(member=self.element2, container=iterated_elements)

    # -----------------------------------------------------------------------------------
    def test_iteration_over_empty_source_file(self) -> None:
        # Operate
        iterated_elements: List[CodeElement] = list(self.source_file)

        # Check
        self.assertEqual(first=len(iterated_elements), second=0)

    # -----------------------------------------------------------------------------------
    def test_for_loop_over_elements(self) -> None:
        # Build
        self.source_file.add_element(element=self.element1)
        self.source_file.add_element(element=self.element2)

        # Operate & Check
        count: int = 0
        for element in self.source_file:
            self.assertIsInstance(obj=element, cls=CodeElement)
            count += 1

        # Check
        self.assertEqual(first=count, second=2)

    # -----------------------------------------------------------------------------------
    def test_contains_check(self) -> None:
        # Build
        self.source_file.add_element(element=self.element1)

        # Check
        self.assertIn(member=self.element1, container=self.source_file)
        self.assertNotIn(member=self.element2, container=self.source_file)


# _______________________________________________________________________________________
class TestSourceFileEquality(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.path: str = "/path/to/file.py"

        self.element: CodeElement = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(
                file_path="/path/to/file.py",
                line_number=10
            )
        )

    # -----------------------------------------------------------------------------------
    def test_source_file_equality_with_same_data(self) -> None:
        # Build
        sf1: SourceFile = SourceFile(path=self.path)
        sf2: SourceFile = SourceFile(path=self.path)

        # Check
        self.assertEqual(first=sf1, second=sf2)

    # -----------------------------------------------------------------------------------
    def test_source_file_equality_with_same_elements(self) -> None:
        # Build
        sf1: SourceFile = SourceFile(path=self.path)
        sf2: SourceFile = SourceFile(path=self.path)

        # Operate
        sf1.add_element(element=self.element)
        sf2.add_element(element=self.element)

        # Check
        self.assertEqual(first=sf1, second=sf2)

    # -----------------------------------------------------------------------------------
    def test_source_file_inequality_different_path(self) -> None:
        # Build
        sf1: SourceFile = SourceFile(path="/path/to/file1.py")
        sf2: SourceFile = SourceFile(path="/path/to/file2.py")

        # Check
        self.assertNotEqual(first=sf1, second=sf2)

    # -----------------------------------------------------------------------------------
    def test_source_file_inequality_different_elements(self) -> None:
        # Build
        sf1: SourceFile = SourceFile(path=self.path)
        sf2: SourceFile = SourceFile(path=self.path)

        # Operate
        sf1.add_element(element=self.element)

        # Check
        self.assertNotEqual(first=sf1, second=sf2)

    # -----------------------------------------------------------------------------------
    def test_source_file_inequality_with_non_source_file_object(self) -> None:
        # Build
        sf: SourceFile = SourceFile(path=self.path)

        # Check
        self.assertNotEqual(first=sf, second="not a source file")
        self.assertNotEqual(first=sf, second=None)
        self.assertNotEqual(first=sf, second=42)
        self.assertNotEqual(first=sf, second={"path": self.path})


# _______________________________________________________________________________________
class TestSourceFileRepr(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.source_file: SourceFile = SourceFile(path="/path/to/file.py")

    # -----------------------------------------------------------------------------------
    def test_source_file_repr_contains_essential_info(self) -> None:
        # Operate
        repr_string: str = repr(self.source_file)

        # Check
        self.assertIn(member="SourceFile", container=repr_string)
        self.assertIn(member="/path/to/file.py", container=repr_string)
        self.assertIn(member="0", container=repr_string)

    # -----------------------------------------------------------------------------------
    def test_source_file_repr_format(self) -> None:
        # Build
        expected: str = "SourceFile(path='/path/to/file.py', elements_count=0)"

        # Operate
        repr_string: str = repr(self.source_file)

        # Check
        self.assertEqual(first=repr_string, second=expected)

    # -----------------------------------------------------------------------------------
    def test_source_file_repr_with_elements(self) -> None:
        # Build
        element: CodeElement = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(
                file_path="/path/to/file.py",
                line_number=10
            )
        )
        expected: str = "SourceFile(path='/path/to/file.py', elements_count=1)"

        # Operate
        self.source_file.add_element(element=element)

        # Check
        self.assertEqual(first=repr(self.source_file), second=expected)


if __name__ == '__main__':
    unittest.main()
