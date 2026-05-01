from initialize_db import initialize_database

def menu():
    while True:
        print("\n=== Banking System ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "5":
            print("Goodbye.")
            break
        else:
            print("Feature not built yet.")

if __name__ == "__main__":
    initialize_database()
    menu()
