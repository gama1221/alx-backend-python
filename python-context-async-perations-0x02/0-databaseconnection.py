#!/usr/bin/python3
import sqlite3

class DatabaseConnection:
    """Custom context manager for SQLite database connections."""
    
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        """Open the database connection."""
        self.conn = sqlite3.connect(self.db_file)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the connection, committing if no exception, otherwise rollback."""
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.conn.close()
        # Returning False will propagate exceptions if any
        return False

# --- Example usage ---
if __name__ == "__main__":
    with DatabaseConnection("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)
