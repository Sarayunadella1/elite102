import sqlite3

DB_NAME = "example.db"

def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        balance REAL NOT NULL
    )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialize_database()
