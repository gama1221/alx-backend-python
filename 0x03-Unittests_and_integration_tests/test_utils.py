#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function in the utils module.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    # Define the inputs for the parameterized tests: (nested_map, path, expected_result)
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test that access_nested_map returns the expected result for various inputs.
        The body should be no longer than 2 lines.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

