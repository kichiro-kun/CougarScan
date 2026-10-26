# -*- coding: utf-8 -*-

"""
TestCases for project_code.domain.location

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'TestLocation'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# =======================================================================================
import unittest
from project_code.domain.location import Location
from typing import Any, List, Tuple


# _______________________________________________________________________________________
class TestLocation(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.valid_file_path = "/path/to/file.py"
        self.valid_line_number = 10
        self.location = Location(
            file_path=self.valid_file_path,
            line_number=self.valid_line_number
        )

    # -----------------------------------------------------------------------------------
    def test_location_creation_with_valid_data(self) -> None:
        # Check
        self.assertEqual(first=self.location.get_file_path(), second=self.valid_file_path)
        self.assertEqual(first=self.location.get_line_number(), second=self.valid_line_number)

    # -----------------------------------------------------------------------------------
    def test_location_creation_with_empty_path_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Operate & Check
            Location(file_path="", line_number=10)

    # -----------------------------------------------------------------------------------
    def test_location_creation_with_negative_line_number_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Operate & Check
            Location(file_path="/path/to/file.py", line_number=-1)

    # -----------------------------------------------------------------------------------
    def test_location_creation_with_zero_line_number_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Operate & Check
            Location(file_path="/path/to/file.py", line_number=0)

    # -----------------------------------------------------------------------------------
    def test_location_equality_with_same_data(self) -> None:
        # Build
        location1 = Location(file_path="/path/to/file.py", line_number=10)
        location2 = Location(file_path="/path/to/file.py", line_number=10)

        # Check
        self.assertEqual(first=location1, second=location2)

    # -----------------------------------------------------------------------------------
    def test_location_equality_with_different_path(self) -> None:
        # Build
        location1 = Location(file_path="/path/to/file1.py", line_number=10)
        location2 = Location(file_path="/path/to/file2.py", line_number=10)

        # Check
        self.assertNotEqual(first=location1, second=location2)

    # -----------------------------------------------------------------------------------
    def test_location_equality_with_different_line(self) -> None:
        # Build
        location1 = Location(file_path="/path/to/file.py", line_number=10)
        location2 = Location(file_path="/path/to/file.py", line_number=20)

        # Check
        self.assertNotEqual(first=location1, second=location2)

    # -----------------------------------------------------------------------------------
    def test_location_equality_with_non_location_object(self) -> None:
        # Build
        non_location_objects: Tuple[Any, ...] = (
            "not a location", None, 67, {"file_path": self.valid_file_path}
        )
        assert_count: int = 0

        # Prepare check context
        for non_location in non_location_objects:
            assert_count += 1
            with self.subTest(msg=f"Assert №{assert_count}: *{non_location}*"):
                # Check
                self.assertNotEqual(
                    first=self.location,
                    second=non_location
                )

    # -----------------------------------------------------------------------------------
    def test_location_repr_contains_essential_info(self) -> None:
        # Extract
        repr_string: str = repr(self.location)

        # Check
        self.assertIn(
            member="Location",
            container=repr_string
        )
        self.assertIn(
            member=self.valid_file_path,
            container=repr_string
        )
        self.assertIn(
            member=str(object=self.valid_line_number),
            container=repr_string
        )

    # -----------------------------------------------------------------------------------
    def test_location_repr_format(self) -> None:
        # Build
        location = Location(file_path="/path/to/file.py", line_number=10)
        expected = "Location(file_path='/path/to/file.py', line_number=10)"

        # Check
        self.assertEqual(first=repr(location), second=expected)

    # -----------------------------------------------------------------------------------
    def test_location_with_different_valid_paths(self) -> None:
        # Build
        expected_paths: List[str] = [
            "/absolute/path.py",
            "relative/path.py",
            "./current/path.py",
            "../parent/path.py",
            "C:\\Windows\\path.py",
            "file.py"
        ]
        assert_count: int = 0

        # Prepare check context
        for expected_path in expected_paths:
            # Operate
            location = Location(file_path=expected_path, line_number=1)

            assert_count += 1
            with self.subTest(msg=f"Assert №{assert_count}: *{location}*"):
                # Extract
                actual_path = location.get_file_path()

                # Check
                self.assertEqual(first=actual_path, second=expected_path)

    # -----------------------------------------------------------------------------------
    def test_location_with_large_line_number(self) -> None:
        # Build
        large_line_number = 999999

        # Operate
        location = Location(file_path="/path/to/file.py", line_number=large_line_number)

        # Check
        self.assertEqual(first=location.get_line_number(), second=large_line_number)


if __name__ == '__main__':
    unittest.main()
