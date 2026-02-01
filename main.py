import os

DATA_FILE = "../data/accounts.txt"


def create_account():
    acc_no = input("Enter account number: ")
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    with open(DATA_FILE, "a") as f:
        f.write(f"{acc_no},{name},{balance}\n")

    print("Account created successfully.")


def deposit():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter deposit amount: "))

    updated = False
    lines = []

    with open(DATA_FILE, "r") as f:
        lines = f.readlines()

    with open(DATA_FILE, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == acc_no:
                data[2] = str(float(data[2]) + amount)
                updated = True
            f.write(",".join(data) + "\n")

    if updated:
        print("Amount deposited successfully.")
    else:
        print("Account not found.")


def withdraw():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter withdrawal amount: "))

    updated = False
    lines = []

    with open(DATA_FILE, "r") as f:
        lines = f.readlines()

    with open(DATA_FILE, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == acc_no:
                balance = float(data[2])
                if balance >= amount:
                    data[2] = str(balance - amount)
                    updated = True
                else:
                    print("Insufficient balance.")
                f.write(",".join(data) + "\n")
            else:
                f.write(line)

    if updated:
        print("Withdrawal successful.")
    else:
        print("Account not found or insufficient balance.")


def check_balance():
    acc_no = input("Enter account number: ")

    with open(DATA_FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == acc_no:
                print(f"Account Holder: {data[1]}")
                print(f"Balance: {data[2]}")
                return

    print("Account not found.")


def view_accounts():
    print("\n--- All Accounts ---")
    with open(DATA_FILE, "r") as f:
        for line in f:
            acc_no, name, balance = line.strip().split(",")
            print(f"Account No: {acc_no}, Name: {name}, Balance: {balance}")


def main():
    if not os.path.exists("../data"):
        os.mkdir("../data")

    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, "w").close()

    while True:
        print("\n--- Banking Automation System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View All Accounts")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_accounts()
        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
