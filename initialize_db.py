import sqlite3

DB_NAME = "example.db"

def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")

    cursor = connection.cursor()
    print("Cursor created.")

    print("Creating table if it does not exist...")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        balance REAL NOT NULL
    )
    """)

    print("Table created.")

    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


initialize_database()
