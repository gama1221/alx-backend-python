# Python Generators - ALX Backend Project

## Project Overview

This project demonstrates how to work with **Python generators** to stream data from a MySQL database efficiently. The goal is to avoid loading large datasets entirely into memory, using a generator to yield one row at a time.

We create a database `ALX_prodev`, populate it with sample user data from `user_data.csv`, and stream rows using a generator function.

---

## Project Structure


---

## Database Schema

**Database:** `ALX_prodev`  
**Table:** `user_data`

| Column   | Type           | Notes                        |
|----------|----------------|-------------------------------|
| user_id  | CHAR(36)       | Primary Key, UUID, Indexed   |
| name     | VARCHAR(255)   | NOT NULL                     |
| email    | VARCHAR(255)   | NOT NULL                     |
| age      | DECIMAL(10,0)  | NOT NULL                     |

---

## Scripts

### `seed.py`

Contains functions to:

- Connect to the MySQL server (`connect_db()`)  
- Create the `ALX_prodev` database (`create_database()`)  
- Connect to the `ALX_prodev` database (`connect_to_prodev()`)  
- Create the `user_data` table (`create_table()`)  
- Populate the table from `user_data.csv` (`insert_data()`)  
- Stream rows using a **generator** (`data_generator()`)

---

### `0-main.py`

Main script that:

1. Connects to MySQL server.  
2. Creates the `ALX_prodev` database if it doesn’t exist.  
3. Connects to the database.  
4. Creates the `user_data` table if it doesn’t exist.  
5. Inserts data from `user_data.csv`.  
6. Demonstrates streaming rows using the generator.  

**Example Output:**


---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/gama1221/alx-backend-python.git
cd alx-backend-python

python3 -m venv venv
source venv/bin/activate

chmod +x 0-main.py
./0-main.py



---

This README clearly documents your **Python generators exercise**, the project structure, usage, and database schema.  

If you want, I can also **add a “How the generator works” diagram** and **example of streaming all rows without loading everything** to make it even more professional for ALX submission.  

Do you want me to do that?
