#!/usr/bin/env python3
"""
1-batch_processing.py

Batch processing for users database
"""

import seed

def stream_users_in_batches(batch_size):
    """
    Generator function to fetch users in batches.
    Yields a list of rows (dictionaries) per batch.
    """
    connection = seed.connect_to_prodev()
    if not connection:
        return

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Processes users in batches and filters users over age 25.
    Yields each user one by one after filtering.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
