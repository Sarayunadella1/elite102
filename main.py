import sqlite3
from initialize_db import initialize_database

DB_NAME = "example.db"

def create_account():
    name = input("Enter name: ")
    deposit = float(input("Initial deposit: "))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO accounts (name, balance) VALUES (?, ?)",
        (name, deposit)
    )

    conn.commit()
    conn.close()

    print("Account created successfully!")

def deposit_money():
    account_id = int(input("Account ID: "))
    amount = float(input("Deposit amount: "))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE id = ?",
        (amount, account_id)
    )

    conn.commit()
    conn.close()

    print("Deposit successful!")

def withdraw_money():
    account_id = int(input("Account ID: "))
    amount = float(input("Withdraw amount: "))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
    result = cursor.fetchone()

    if result and result[0] >= amount:
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, account_id)
        )
        print("Withdrawal successful!")
    else:
        print("Insufficient funds or account not found.")

    conn.commit()
    conn.close()

def check_balance():
    account_id = int(input("Account ID: "))

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        print(f"Balance: ${result[0]}")
    else:
        print("Account not found.")

def menu():
    while True:
        print("\n=== Banking System ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    initialize_database()
    menu()
