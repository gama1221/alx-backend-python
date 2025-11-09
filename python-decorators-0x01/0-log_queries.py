#!/usr/bin/python3
"""
0-log_queries.py
Decorator to log SQL queries executed by a function.
"""
import sqlite3
import functools

def log_queries(func):
    """Decorator that logs the SQL query before executing the function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check if 'query' is passed as a keyword argument
        query = kwargs.get('query', None)
        if query is None and len(args) > 0:
            query = args[0]  # Assume first positional arg is the query

        if query:
            print(f"[LOG] Executing SQL Query: {query}")

        return func(*args, **kwargs)

    return wrapper

@log_queries
def fetch_all_users(query):
    """Executes the given SQL query and returns all rows."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    # Example usage
    users = fetch_all_users(query="SELECT * FROM users")
    print(f"Fetched {len(users)} users")
