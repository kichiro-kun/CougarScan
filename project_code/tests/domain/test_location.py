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
__version__ = '0.2.0'


# =======================================================================================
import unittest
from project_code.domain.location import Location
from typing import Any, Dict, List, Tuple


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


# _______________________________________________________________________________________
class TestLocationHashing(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def test_location_is_hashable(self) -> None:
        # Build
        location = Location(file_path="/path/to/file.py", line_number=10)

        # Operate
        hash_value: int = hash(location)

        # Check
        self.assertIsInstance(obj=hash_value, cls=int)

    # -----------------------------------------------------------------------------------
    def test_equal_locations_have_equal_hashes(self) -> None:
        # Build
        location1 = Location(file_path="/path/to/file.py", line_number=10)
        location2 = Location(file_path="/path/to/file.py", line_number=10)

        # Check
        self.assertEqual(first=location1, second=location2)
        self.assertEqual(first=hash(location1), second=hash(location2))

    # -----------------------------------------------------------------------------------
    def test_different_locations_have_different_hashes(self) -> None:
        # Build
        location1 = Location(file_path="/path/to/file1.py", line_number=10)
        location2 = Location(file_path="/path/to/file2.py", line_number=10)
        location3 = Location(file_path="/path/to/file.py", line_number=20)

        # Check
        self.assertNotEqual(first=hash(location1), second=hash(location2))
        self.assertNotEqual(first=hash(location1), second=hash(location3))
        self.assertNotEqual(first=hash(location2), second=hash(location3))

    # -----------------------------------------------------------------------------------
    def test_hash_is_stable(self) -> None:
        # Build
        location = Location(file_path="/path/to/file.py", line_number=10)

        # Prepare data
        hash1: int = hash(location)
        hash2: int = hash(location)
        hash3: int = hash(location)

        # Check
        self.assertEqual(first=hash1, second=hash2)
        self.assertEqual(first=hash2, second=hash3)

    # -----------------------------------------------------------------------------------
    def test_location_can_be_added_to_set(self) -> None:
        # Build
        location1 = Location(file_path="/path/to/file.py", line_number=10)
        location2 = Location(file_path="/path/to/file.py", line_number=10)
        location3 = Location(file_path="/path/to/file.py", line_number=20)

        # Operate
        location_set: set[Location] = {location1, location2, location3}

        # Check
        # location1 и location2 равны, поэтому set должен содержать только 2 элемента
        self.assertEqual(first=len(location_set), second=2)

    # -----------------------------------------------------------------------------------
    def test_location_can_be_used_as_dict_key(self) -> None:
        # Build
        location = Location(file_path="/path/to/file.py", line_number=10)

        # Operate
        dictionary: Dict[Location, str] = {location: "value"}

        # Check
        self.assertEqual(first=dictionary[location], second="value")

    # -----------------------------------------------------------------------------------
    def test_equal_locations_map_to_same_dict_value(self) -> None:
        # Build
        location1 = Location(file_path="/path/to/file.py", line_number=10)
        location2 = Location(file_path="/path/to/file.py", line_number=10)

        # Operate
        dictionary: Dict[Location, str] = {location1: "value"}

        # Check
        self.assertEqual(first=dictionary[location2], second="value")


if __name__ == '__main__':
    unittest.main()
