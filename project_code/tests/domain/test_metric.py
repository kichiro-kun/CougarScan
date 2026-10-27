# -*- coding: utf-8 -*-

"""
TestCases for project_code.domain.metric

Copyright 2026 kichiro-kun (Kei)
Apache license, version 2.0 (Apache-2.0 license)
"""

__all__: list[str] = [
    'TestMetricCreation',
    'TestMetricGetters',
    'TestMetricEquality',
    'TestMetricHashing',
    'TestMetricRepr'
]

__author__ = 'kichiro-kun (Kei)'
__version__ = '0.1.0'


# =======================================================================================
import unittest
from project_code.domain.metric import Metric
from project_code.domain.code_element import CodeElement
from project_code.domain.location import Location
from project_code.domain.enums import ElementType


# _______________________________________________________________________________________
class TestMetricCreation(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.target_element: CodeElement = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        self.valid_name: str = "Cyclomatic Complexity"
        self.valid_value: float = 5.0

    # -----------------------------------------------------------------------------------
    def test_metric_creation_with_valid_data(self) -> None:
        # Build
        metric: Metric = Metric(
            name=self.valid_name,
            value=self.valid_value,
            target_element=self.target_element
        )

        # Check
        self.assertEqual(first=metric.get_name(), second=self.valid_name)
        self.assertEqual(first=metric.get_value(), second=self.valid_value)
        self.assertEqual(first=metric.get_target(), second=self.target_element)

    # -----------------------------------------------------------------------------------
    def test_metric_creation_with_empty_name_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Check
            Metric(
                name="",
                value=self.valid_value,
                target_element=self.target_element
            )

    # -----------------------------------------------------------------------------------
    def test_metric_creation_with_none_name_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Check
            Metric(
                name=None,  # type: ignore
                value=self.valid_value,
                target_element=self.target_element
            )

    # -----------------------------------------------------------------------------------
    def test_metric_creation_with_negative_value_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=ValueError):
            # Check
            Metric(
                name=self.valid_name,
                value=-1.0,
                target_element=self.target_element
            )

    # -----------------------------------------------------------------------------------
    def test_metric_creation_with_none_value_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Check
            Metric(
                name=self.valid_name,
                value=None,  # type: ignore
                target_element=self.target_element
            )

    # -----------------------------------------------------------------------------------
    def test_metric_creation_with_boolean_true_value_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Check
            Metric(
                name=self.valid_name,
                value=True,
                target_element=self.target_element
            )

    # -----------------------------------------------------------------------------------
    def test_metric_creation_with_boolean_false_value_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Check
            Metric(
                name=self.valid_name,
                value=False,
                target_element=self.target_element
            )

    # -----------------------------------------------------------------------------------
    def test_metric_creation_with_string_value_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Check
            Metric(
                name=self.valid_name,
                value="5.0",  # type: ignore
                target_element=self.target_element
            )

    # -----------------------------------------------------------------------------------
    def test_metric_creation_with_none_target_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Check
            Metric(
                name=self.valid_name,
                value=self.valid_value,
                target_element=None  # type: ignore
            )

    # -----------------------------------------------------------------------------------
    def test_metric_creation_with_non_code_element_target_raises_error(self) -> None:
        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Check
            Metric(
                name=self.valid_name,
                value=self.valid_value,
                target_element="not a code element"  # type: ignore
            )

        # Prepare check context
        with self.assertRaises(expected_exception=TypeError):
            # Check
            Metric(
                name=self.valid_name,
                value=self.valid_value,
                target_element=42  # type: ignore
            )

    # -----------------------------------------------------------------------------------
    def test_metric_with_zero_value(self) -> None:
        # Build
        metric: Metric = Metric(
            name="Lines of Code",
            value=0.0,
            target_element=self.target_element
        )

        # Check
        self.assertEqual(first=metric.get_value(), second=0.0)

    # -----------------------------------------------------------------------------------
    def test_metric_with_integer_value(self) -> None:
        # Build
        metric: Metric = Metric(
            name="Lines of Code",
            value=42,
            target_element=self.target_element
        )

        # Check
        self.assertEqual(first=metric.get_value(), second=42)

    # -----------------------------------------------------------------------------------
    def test_metric_with_large_value(self) -> None:
        # Build
        large_value: float = 999999.99
        metric: Metric = Metric(
            name="Large Metric",
            value=large_value,
            target_element=self.target_element
        )

        # Check
        self.assertEqual(first=metric.get_value(), second=large_value)

    # -----------------------------------------------------------------------------------
    def test_metric_with_various_names(self) -> None:
        # Build
        names: list[str] = [
            "Cyclomatic Complexity",
            "Lines of Code",
            "Number of Methods",
            "Afferent Couplings",
            "Efferent Couplings",
            "ABC Metric"
        ]
        assert_count: int = 0

        # Prepare check context
        for name in names:
            assert_count += 1
            with self.subTest(msg=f"Assert №{assert_count}: *{name}*"):
                # Operate
                metric: Metric = Metric(
                    name=name,
                    value=1.0,
                    target_element=self.target_element
                )

                # Check
                self.assertEqual(first=metric.get_name(), second=name)

    # -----------------------------------------------------------------------------------
    def test_metric_with_different_element_types(self) -> None:
        # Build
        assert_count: int = 0

        # Prepare check context
        for element_type in ElementType:
            assert_count += 1
            with self.subTest(msg=f"Assert №{assert_count}: *{element_type}*"):
                # Build
                element: CodeElement = CodeElement(
                    name=f"element_{element_type.value}",
                    element_type=element_type,
                    location=Location(file_path="/path/to/file.py", line_number=10)
                )

                # Operate
                metric: Metric = Metric(
                    name="Test Metric",
                    value=1.0,
                    target_element=element
                )

                # Check
                self.assertEqual(first=metric.get_target(), second=element)


# _______________________________________________________________________________________
class TestMetricGetters(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.target_element: CodeElement = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        self.metric: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )

    # -----------------------------------------------------------------------------------
    def test_get_name_returns_correct_value(self) -> None:
        # Check
        self.assertEqual(first=self.metric.get_name(), second="Cyclomatic Complexity")

    # -----------------------------------------------------------------------------------
    def test_get_value_returns_correct_value(self) -> None:
        # Check
        self.assertEqual(first=self.metric.get_value(), second=5.0)

    # -----------------------------------------------------------------------------------
    def test_get_target_returns_correct_value(self) -> None:
        # Check
        self.assertEqual(first=self.metric.get_target(), second=self.target_element)

    # -----------------------------------------------------------------------------------
    def test_get_target_returns_same_object(self) -> None:
        # Extract
        returned_target: CodeElement = self.metric.get_target()

        # Check
        self.assertIs(expr1=returned_target, expr2=self.target_element)


# _______________________________________________________________________________________
class TestMetricEquality(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.target_element: CodeElement = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )

    # -----------------------------------------------------------------------------------
    def test_metric_equality_with_same_data(self) -> None:
        # Build
        metric1: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )
        metric2: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )

        # Check
        self.assertEqual(first=metric1, second=metric2)

    # -----------------------------------------------------------------------------------
    def test_metric_equality_with_equal_targets(self) -> None:
        # Build
        target1: CodeElement = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        target2: CodeElement = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )

        # Prepare instances
        metric1: Metric = Metric(name="Metric", value=5.0, target_element=target1)
        metric2: Metric = Metric(name="Metric", value=5.0, target_element=target2)

        # Check
        self.assertEqual(first=metric1, second=metric2)

    # -----------------------------------------------------------------------------------
    def test_metric_inequality_different_name(self) -> None:
        # Build
        metric1: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )
        metric2: Metric = Metric(
            name="Lines of Code",
            value=5.0,
            target_element=self.target_element
        )

        # Check
        self.assertNotEqual(first=metric1, second=metric2)

    # -----------------------------------------------------------------------------------
    def test_metric_inequality_different_value(self) -> None:
        # Build
        metric1: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )
        metric2: Metric = Metric(
            name="Cyclomatic Complexity",
            value=10.0,
            target_element=self.target_element
        )

        # Check
        self.assertNotEqual(first=metric1, second=metric2)

    # -----------------------------------------------------------------------------------
    def test_metric_inequality_different_target(self) -> None:
        # Build
        target1: CodeElement = CodeElement(
            name="function1",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        target2: CodeElement = CodeElement(
            name="function2",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=20)
        )

        # Prepare instances
        metric1: Metric = Metric(name="Metric", value=5.0, target_element=target1)
        metric2: Metric = Metric(name="Metric", value=5.0, target_element=target2)

        # Check
        self.assertNotEqual(first=metric1, second=metric2)

    # -----------------------------------------------------------------------------------
    def test_metric_inequality_with_non_metric_object(self) -> None:
        # Build
        metric: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )

        # Check
        self.assertNotEqual(first=metric, second="not a metric")
        self.assertNotEqual(first=metric, second=None)
        self.assertNotEqual(first=metric, second=42)
        self.assertNotEqual(first=metric, second={"name": "Cyclomatic Complexity"})


# _______________________________________________________________________________________
class TestMetricHashing(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.target_element: CodeElement = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )

    # -----------------------------------------------------------------------------------
    def test_metric_is_hashable(self) -> None:
        # Build
        metric: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )

        # Operate
        hash_value: int = hash(metric)

        # Check
        self.assertIsInstance(obj=hash_value, cls=int)

    # -----------------------------------------------------------------------------------
    def test_equal_metrics_have_equal_hashes(self) -> None:
        # Build
        metric1: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )
        metric2: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )

        # Check
        self.assertEqual(first=metric1, second=metric2)
        self.assertEqual(first=hash(metric1), second=hash(metric2))

    # -----------------------------------------------------------------------------------
    def test_different_metrics_have_different_hashes(self) -> None:
        # Build
        metric1: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )
        metric2: Metric = Metric(
            name="Lines of Code",
            value=5.0,
            target_element=self.target_element
        )
        metric3: Metric = Metric(
            name="Cyclomatic Complexity",
            value=10.0,
            target_element=self.target_element
        )

        # Check
        self.assertNotEqual(first=hash(metric1), second=hash(metric2))
        self.assertNotEqual(first=hash(metric1), second=hash(metric3))
        self.assertNotEqual(first=hash(metric2), second=hash(metric3))

    # -----------------------------------------------------------------------------------
    def test_hash_is_stable(self) -> None:
        # Build
        metric: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )

        # Operate
        hash1: int = hash(metric)
        hash2: int = hash(metric)
        hash3: int = hash(metric)

        # Check
        self.assertEqual(first=hash1, second=hash2)
        self.assertEqual(first=hash2, second=hash3)

    # -----------------------------------------------------------------------------------
    def test_metric_can_be_added_to_set(self) -> None:
        # Build
        metric1: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )
        metric2: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )
        metric3: Metric = Metric(
            name="Lines of Code",
            value=10.0,
            target_element=self.target_element
        )

        # Operate
        metric_set: set[Metric] = {metric1, metric2, metric3}

        # Check
        # metric1 и metric2 равны, поэтому set должен содержать только 2 элемента
        self.assertEqual(first=len(metric_set), second=2)

    # -----------------------------------------------------------------------------------
    def test_metric_can_be_used_as_dict_key(self) -> None:
        # Build
        metric: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )

        # Operate
        dictionary: dict[Metric, str] = {metric: "value"}

        # Check
        self.assertEqual(first=dictionary[metric], second="value")

    # -----------------------------------------------------------------------------------
    def test_equal_metrics_map_to_same_dict_value(self) -> None:
        # Build
        metric1: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )
        metric2: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )

        # Operate
        dictionary: dict[Metric, str] = {metric1: "value"}

        # Check
        self.assertEqual(first=dictionary[metric2], second="value")


# _______________________________________________________________________________________
class TestMetricRepr(unittest.TestCase):

    # -----------------------------------------------------------------------------------
    def setUp(self) -> None:
        self.target_element: CodeElement = CodeElement(
            name="my_function",
            element_type=ElementType.FUNCTION,
            location=Location(file_path="/path/to/file.py", line_number=10)
        )
        self.metric: Metric = Metric(
            name="Cyclomatic Complexity",
            value=5.0,
            target_element=self.target_element
        )

    # -----------------------------------------------------------------------------------
    def test_metric_repr_contains_essential_info(self) -> None:
        # Extract
        repr_string: str = repr(self.metric)

        # Check
        self.assertIn(member="Metric", container=repr_string)
        self.assertIn(member="Cyclomatic Complexity", container=repr_string)
        self.assertIn(member="5.0", container=repr_string)
        self.assertIn(member="my_function", container=repr_string)

    # -----------------------------------------------------------------------------------
    def test_metric_repr_format(self) -> None:
        # Build
        expected: str = (
            "Metric(name='Cyclomatic Complexity', "
            "value=5.0, "
            "target=CodeElement(name='my_function', "
            "element_type=ElementType.FUNCTION, "
            "location=Location(file_path='/path/to/file.py', line_number=10)))"
        )

        # Check
        self.assertEqual(first=repr(self.metric), second=expected)


if __name__ == '__main__':
    unittest.main()
