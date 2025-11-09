#!/usr/bin/env python3

"""
seed.py
Sets up the MySQL database ALX_prodev and populates the user_data table.
"""
import mysql.connector
from mysql.connector import errorcode
import csv
import uuid

# --- Configuration ---
# NOTE: Replace with your actual MySQL credentials
MYSQL_USER = "root"  # e.g., "root"
MYSQL_PASSWORD = "Nacos@12345!"
MYSQL_HOST = "localhost"
DATABASE_NAME = "ALX_prodev"

# --- Database Schema ---
TABLE_NAME = "user_data"
TABLE_SCHEMA = (
    f"CREATE TABLE {TABLE_NAME} ("
    "    user_id CHAR(36) PRIMARY KEY,"  # Using CHAR(36) for UUID
    "    name VARCHAR(255) NOT NULL,"
    "    email VARCHAR(255) NOT NULL,"
    "    age DECIMAL(10, 0) NOT NULL"
    ") ENGINE=InnoDB"
)

# --- Prototype Functions ---

def connect_db():
    """Connects to the MySQL database server."""
    try:
        connection = mysql.connector.connect(
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST
        )
        print("Connected to MySQL server successfully")

        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username/password.")
        else:
            print(f"Error connecting to MySQL server: {err}")
        return None

def create_database(connection):
    """Creates the database ALX_prodev if it does not exist."""
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME} DEFAULT CHARACTER SET 'utf8'")
        print(f"Database {DATABASE_NAME} created successfully or already exists.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    """Connects to the ALX_prodev database in MySQL."""
    try:
        connection = mysql.connector.connect(
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host=MYSQL_HOST,
            database=DATABASE_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database {DATABASE_NAME}: {err}")
        return None

def create_table(connection):
    """Creates a table user_data if it does not exist with the required fields."""
    cursor = connection.cursor()
    try:
        cursor.execute(TABLE_SCHEMA)
        print(f"Table {TABLE_NAME} created successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print(f"Table {TABLE_NAME} already exists.")
        else:
            print(f"Error creating table: {err.msg}")
    finally:
        cursor.close()

def data_generator(filepath):
    """
    Generator function to stream rows from the CSV file.
    This fulfills the objective of creating a generator.
    """
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            # Generate a new UUID for the primary key
            row.insert(0, str(uuid.uuid4()))
            yield row

def insert_data(connection, filepath):
    """Inserts data into the database from the CSV file."""
    cursor = connection.cursor()
    
    # Check if the table is empty to avoid double insertion
    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    if cursor.fetchone()[0] > 0:
        print(f"Table {TABLE_NAME} already contains data. Skipping insertion.")
        cursor.close()
        return

    insert_query = (
        f"INSERT INTO {TABLE_NAME} "
        "(user_id, name, email, age) "
        "VALUES (%s, %s, %s, %s)"
    )
    
    # Use the generator to stream data to the database
    data = data_generator(filepath)
    
    try:
        # Fetch the entire data list from the generator to use executemany
        # Note: For truly massive datasets, you might commit in chunks
        data_to_insert = list(data)
        
        if data_to_insert:
            cursor.executemany(insert_query, data_to_insert)
            connection.commit()
            print(f"Inserted {len(data_to_insert)} rows into {TABLE_NAME} successfully.")
        else:
            print("No data found in the CSV file to insert.")

    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
        connection.rollback()
    finally:
        cursor.close()