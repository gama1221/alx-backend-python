#!/usr/bin/env python3
"""
1-main.py
Demonstrates streaming rows from the user_data table using the generator
from 0-stream_users.py.
"""

from itertools import islice
stream_users_module = __import__('0-stream_users')

if __name__ == "__main__":
    # Create the generator
    users_generator = stream_users_module.stream_users()

    # Print the first 6 rows from the generator
    for user in islice(users_generator, 6):
        print(user)
