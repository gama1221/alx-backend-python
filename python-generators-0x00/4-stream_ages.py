#!/usr/bin/python3
"""
4-stream_ages.py
Memory-efficient aggregation using generators to compute average age.
"""
import seed

def stream_user_ages():
    """Generator that yields user ages one by one from the database."""
    connection = seed.connect_to_prodev()
    if not connection:
        return

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    
    for row in cursor:
        yield row['age']  # Yield age one by one

    cursor.close()
    connection.close()

def calculate_average_age():
    """Calculate average age using the generator without loading all rows into memory."""
    total_age = 0
    count = 0

    for age in stream_user_ages():  # Loop 1: iterate generator
        total_age += age
        count += 1

    if count == 0:
        print("No users found in the database.")
        return

    average_age = total_age / count
    print(f"Average age of users: {average_age:.2f}")

if __name__ == "__main__":
    calculate_average_age()
