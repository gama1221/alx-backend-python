#!/usr/bin/python3
"""
2-lazy_paginate.py
Lazy loads paginated data from user_data table using a generator.
"""
import seed

def paginate_users(page_size, offset):
    """
    Fetches a page of users from the database starting at the given offset.
    Returns a list of dictionaries.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def lazy_pagination(page_size):
    """
    Generator function to lazily fetch users page by page.
    Yields each page (list of user dictionaries).
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
