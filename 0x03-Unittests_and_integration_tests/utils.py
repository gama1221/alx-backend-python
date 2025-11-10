#!/usr/bin/env python3
"""
Utility functions for ALX backend unit tests.
"""


def access_nested_map(nested_map, path):
    """
    Access a nested map (dict) using a sequence of keys.

    Args:
        nested_map (dict): The dictionary to traverse.
        path (tuple): A sequence of keys to follow in the nested map.

    Returns:
        The value found at the nested path.

    Raises:
        KeyError: If any key in the path does not exist.
    """
    current = nested_map
    for key in path:
        if not isinstance(current, dict) or key not in current:
            raise KeyError(key)
        current = current[key]
    return current

def get_json(url):
    """
    Get JSON payload from a URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        dict: JSON response.
    """
    response = requests.get(url)
    return response.json()