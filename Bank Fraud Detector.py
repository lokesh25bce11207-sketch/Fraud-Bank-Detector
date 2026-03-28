Accounts = {
    1001: ["A001", "Saving", 5000, "Delhi"],
    1002: ["A002", "Current", 10000, "Mumbai"]
}

def fraud_check(amount):
    threshold = 3500
    if amount >= threshold:
        print("\n SECURITY ALERT: Transaction blocked!")
        print(f"Reason: Amount ${amount} exceeds the safety limit of ${threshold}.")
        return True 
    return False  

def display_accounts():
    print("\n--- Current Account Database ---")
    for key, value in Accounts.items():
        print(f"ID: {key} | Acc: {value[0]} | Type: {value[1]} | Balance: ${value[2]} | Branch: {value[3]}")
    print("-" * 32)

def deposit():
    accno = input("Enter Account Number: ")
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
            
        for key in Accounts:
            if Accounts[key][0] == accno:
                Accounts[key][2] += amount
                print(f"Successfully deposited ${amount}. New Balance: ${Accounts[key][2]}")
                return
        print("Error: Account not found.")
    except ValueError:
        print("Invalid input. Please enter a numerical value for the amount.")

def withdraw():
    accno = input("Enter Account Number: ")
    try:
        amount = float(input("Enter withdraw amount: "))
        if fraud_check(amount):
            return 
        for key in Accounts:
            if Accounts[key][0] == accno:
                if Accounts[key][2] >= amount:
                    Accounts[key][2] -= amount
                    print(f"Withdrawal successful. Remaining Balance: ${Accounts[key][2]}")
                else:
                    print("Error: Insufficient Balance.")
                return
        print("Error: Account not found.")
    except ValueError:
        print("Invalid input. Please enter a numerical value for the amount.")

def check_balance():
    accno = input("Enter Account Number: ")
    for key in Accounts:
        if Accounts[key][0] == accno:
            print(f"Account {accno} Balance: ${Accounts[key][2]}")
            return
    print("Error: Account not found.")
    
while True:
    print("\nAI BANK MANAGEMENT SYSTEM (Lightweight)")
    print("1. Display Accounts")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter choice: ") 

    if choice == '1':
        display_accounts()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid selection. Please try again.")