#!/usr/bin/env python3
"""
0-stream_users.py
Generator function to stream rows from the user_data table one by one
using the connection from seed.py.
"""

import seed  # Import your seed.py

TABLE_NAME = "user_data"

def stream_users():
    """Generator function that yields one user row at a time as a dictionary."""
    connection = None
    cursor = None
    try:
        connection = seed.connect_to_prodev()
        if connection is None:
            print("Failed to connect to database.")
            return

        cursor = connection.cursor(buffered=True, dictionary=True)
        cursor.execute(f"SELECT * FROM {TABLE_NAME}")

        for row in cursor:
            yield row  # Yield one row at a time

    except Exception as err:
        print(f"Error fetching data: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
