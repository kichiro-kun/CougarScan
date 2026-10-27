# -*- coding: utf-8 -*-

"""
TestCases for project_code.domain.dependency

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'TestDependencyCreation',
    'TestDependencySelfReference',
    'TestDependencyEquality',
    'TestDependencyHashing',
    'TestDependencyRepr'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# =======================================================================================
import unittest
from project_code.domain.dependency import Dependency
from project_code.domain.code_element import CodeElement
from project_code.domain.location import Location
from project_code.domain.enums import ElementType, DependencyType


# _______________________________________________________________________________________
class TestDependencyCreation(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.source_element: CodeElement = CodeElement(
            name="source_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        self.target_element: CodeElement = CodeElement(
            name="target_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )
        self.valid_type: DependencyType = DependencyType.FUNCTION_CALL

    # -----------------------------------------------------------------------------------
    def test_dependency_creation_with_valid_data(self) -> None:
        # Build
        dependency: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=self.valid_type
        )

        # Check
        self.assertEqual(first=dependency.get_source(), second=self.source_element)
        self.assertEqual(first=dependency.get_target(), second=self.target_element)
        self.assertEqual(first=dependency.get_type(), second=self.valid_type)

    # -----------------------------------------------------------------------------------
    def test_dependency_creation_with_none_source_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            Dependency(
                source=None,  # type: ignore
                target=self.target_element,
                dependency_type=self.valid_type
            )

    # -----------------------------------------------------------------------------------
    def test_dependency_creation_with_non_source_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            Dependency(
                source="non_source",  # type: ignore
                target=self.target_element,
                dependency_type=self.valid_type
            )

    # -----------------------------------------------------------------------------------
    def test_dependency_creation_with_non_target_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            Dependency(
                source=self.source_element,
                target="non_target",  # type: ignore
                dependency_type=self.valid_type
            )

    # -----------------------------------------------------------------------------------
    def test_dependency_creation_with_none_target_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            Dependency(
                source=self.source_element,
                target=None,  # type: ignore
                dependency_type=self.valid_type
            )

    # -----------------------------------------------------------------------------------
    def test_dependency_creation_with_invalid_type_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Operate & Check
            Dependency(
                source=self.source_element,
                target=self.target_element,
                dependency_type="invalid_type"  # type: ignore
            )

    # -----------------------------------------------------------------------------------
    def test_dependency_creation_with_none_type_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            Dependency(
                source=self.source_element,
                target=self.target_element,
                dependency_type=None  # type: ignore
            )

    # -----------------------------------------------------------------------------------
    def test_dependency_creation_with_all_dependency_types(self) -> None:
        # Prepare check context
        for dep_type in DependencyType:
            # Build
            dependency: Dependency = Dependency(
                source=self.source_element,
                target=self.target_element,
                dependency_type=dep_type
            )

            # Check
            self.assertEqual(first=dependency.get_type(), second=dep_type)


# _______________________________________________________________________________________
class TestDependencySelfReference(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.element: CodeElement = CodeElement(
            name="recursive_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )

    # -----------------------------------------------------------------------------------
    def test_dependency_self_reference_allowed(self) -> None:
        # Build
        dependency: Dependency = Dependency(
            source=self.element,
            target=self.element,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Check
        self.assertEqual(first=dependency.get_source(), second=dependency.get_target())
        self.assertIs(expr1=dependency.get_source(), expr2=dependency.get_target())

    # -----------------------------------------------------------------------------------
    def test_dependency_self_reference_with_all_types(self) -> None:
        # Prepare check context
        for dep_type in DependencyType:
            # Build
            dependency: Dependency = Dependency(
                source=self.element,
                target=self.element,
                dependency_type=dep_type
            )

            # Check
            self.assertEqual(first=dependency.get_source(), second=dependency.get_target())


# _______________________________________________________________________________________
class TestDependencyEquality(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.source_element: CodeElement = CodeElement(
            name="source_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        self.target_element: CodeElement = CodeElement(
            name="target_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )

    # -----------------------------------------------------------------------------------
    def test_dependency_equality_with_same_data(self) -> None:
        # Build
        dep1: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )
        dep2: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Check
        self.assertEqual(first=dep1, second=dep2)

    # -----------------------------------------------------------------------------------
    def test_dependency_equality_with_equal_elements(self) -> None:
        # Build
        source1: CodeElement = CodeElement(
            name="source_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        source2: CodeElement = CodeElement(
            name="source_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        target1: CodeElement = CodeElement(
            name="target_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )
        target2: CodeElement = CodeElement(
            name="target_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )

        # Prepare instances
        dep1: Dependency = Dependency(
            source=source1,
            target=target1,
            dependency_type=DependencyType.FUNCTION_CALL
        )
        dep2: Dependency = Dependency(
            source=source2,
            target=target2,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Check
        self.assertEqual(first=dep1, second=dep2)

    # -----------------------------------------------------------------------------------
    def test_dependency_inequality_different_source(self) -> None:
        # Build
        source1: CodeElement = CodeElement(
            name="source1",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        source2: CodeElement = CodeElement(
            name="source2",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=15)
        )

        # Prepare instances
        dep1: Dependency = Dependency(
            source=source1,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )
        dep2: Dependency = Dependency(
            source=source2,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Check
        self.assertNotEqual(first=dep1, second=dep2)

    # -----------------------------------------------------------------------------------
    def test_dependency_inequality_different_target(self) -> None:
        # Build
        target1: CodeElement = CodeElement(
            name="target1",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )
        target2: CodeElement = CodeElement(
            name="target2",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=25)
        )

        # Prepare instances
        dep1: Dependency = Dependency(
            source=self.source_element,
            target=target1,
            dependency_type=DependencyType.FUNCTION_CALL
        )
        dep2: Dependency = Dependency(
            source=self.source_element,
            target=target2,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Check
        self.assertNotEqual(first=dep1, second=dep2)

    # -----------------------------------------------------------------------------------
    def test_dependency_inequality_different_type(self) -> None:
        # Build
        dep1: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )
        dep2: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.IMPORT
        )

        # Check
        self.assertNotEqual(first=dep1, second=dep2)

    # -----------------------------------------------------------------------------------
    def test_dependency_inequality_with_non_dependency_object(self) -> None:
        # Build
        dep: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Check
        self.assertNotEqual(first=dep, second="not a dependency")
        self.assertNotEqual(first=dep, second=None)
        self.assertNotEqual(first=dep, second=42)
        self.assertNotEqual(first=dep, second={"source": self.source_element})


# _______________________________________________________________________________________
class TestDependencyHashing(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.source_element: CodeElement = CodeElement(
            name="source_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        self.target_element: CodeElement = CodeElement(
            name="target_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )

    # -----------------------------------------------------------------------------------
    def test_dependency_is_hashable(self) -> None:
        # Build
        dep: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Operate
        hash_value: int = hash(dep)

        # Check
        self.assertIsInstance(obj=hash_value, cls=int)

    # -----------------------------------------------------------------------------------
    def test_equal_dependencies_have_equal_hashes(self) -> None:
        # Build
        dep1: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )
        dep2: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Check
        self.assertEqual(first=dep1, second=dep2)
        self.assertEqual(first=hash(dep1), second=hash(dep2))

    # -----------------------------------------------------------------------------------
    def test_different_dependencies_have_different_hashes(self) -> None:
        # Build
        dep1: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )
        dep2: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.IMPORT
        )

        # Check
        self.assertNotEqual(first=hash(dep1), second=hash(dep2))

    # -----------------------------------------------------------------------------------
    def test_hash_is_stable(self) -> None:
        # Build
        dep: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Operate
        hash1: int = hash(dep)
        hash2: int = hash(dep)
        hash3: int = hash(dep)

        # Check
        self.assertEqual(first=hash1, second=hash2)
        self.assertEqual(first=hash2, second=hash3)

    # -----------------------------------------------------------------------------------
    def test_dependency_can_be_added_to_set(self) -> None:
        # Build
        dep1: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )
        dep2: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )
        dep3: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.IMPORT
        )

        # Operate
        dep_set: set[Dependency] = {dep1, dep2, dep3}

        # Check
        # dep1 и dep2 равны, поэтому set должен содержать только 2 элемента
        self.assertEqual(first=len(dep_set), second=2)

    # -----------------------------------------------------------------------------------
    def test_dependency_can_be_used_as_dict_key(self) -> None:
        # Build
        dep: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Operate
        dictionary: dict[Dependency, str] = {dep: "value"}

        # Check
        self.assertEqual(first=dictionary[dep], second="value")

    # -----------------------------------------------------------------------------------
    def test_equal_dependencies_map_to_same_dict_value(self) -> None:
        # Build
        dep1: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )
        dep2: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )

        # Operate
        dictionary: dict[Dependency, str] = {dep1: "value"}

        # Check
        self.assertEqual(first=dictionary[dep2], second="value")


# _______________________________________________________________________________________
class TestDependencyRepr(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.source_element: CodeElement = CodeElement(
            name="source_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        self.target_element: CodeElement = CodeElement(
            name="target_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )
        self.dependency: Dependency = Dependency(
            source=self.source_element,
            target=self.target_element,
            dependency_type=DependencyType.FUNCTION_CALL
        )

    # -----------------------------------------------------------------------------------
    def test_dependency_repr_contains_essential_info(self) -> None:
        # Extract
        repr_string: str = repr(self.dependency)

        # Check
        self.assertIn(member="Dependency", container=repr_string)
        self.assertIn(member="source_function", container=repr_string)
        self.assertIn(member="target_function", container=repr_string)
        self.assertIn(member="FUNCTION_CALL", container=repr_string)

    # -----------------------------------------------------------------------------------
    def test_dependency_repr_format(self) -> None:
        # Build
        expected: str = (
            "Dependency(source=CodeElement(name='source_function', "
            "element_type=ElementType.FUNCTION, "
            "location=Location(file_path='/path/to/file.py', line_number=10)), "
            "target=CodeElement(name='target_function', "
            "element_type=ElementType.FUNCTION, "
            "location=Location(file_path='/path/to/file.py', line_number=20)), "
            "dependency_type=DependencyType.FUNCTION_CALL)"
        )

        # Check
        self.assertEqual(first=repr(self.dependency), second=expected)


if __name__ == '__main__':
    unittest.main()
