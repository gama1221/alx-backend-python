#!/usr/bin/env python3

import seed  # Better than __import__

if __name__ == '__main__':
    # Connect to MySQL server
    connection = seed.connect_db()
    if connection:
        seed.create_database(connection)
        connection.close()
        print("Database connection and creation checked.")

        # Connect to the ALX_prodev database
        connection = seed.connect_to_prodev()
        if connection:
            seed.create_table(connection)
            seed.insert_data(connection, 'user_data.csv')
            
            # Simple check
            cursor = connection.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {seed.TABLE_NAME};")  # <--- fixed reference
            count = cursor.fetchone()[0]
            print(f"Total rows in {seed.TABLE_NAME}: {count}")
            
            # Example of generator usage
            print("\n--- Testing Data Streaming with Generator ---")
            data_stream = seed.data_generator('user_data.csv')
            print(f"First 3 generated rows (including new UUID):")
            for _ in range(3):
                try:
                    print(next(data_stream))
                except StopIteration:
                    break
                    
            cursor.close()
            connection.close()
