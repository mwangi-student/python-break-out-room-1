def safaricom_menu():
    """Main menu function for Safaricom SIM Toolkit."""
    while True:
        print("SIM 1")
        print("1. Safaricom")
        print("2. M-PESA")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Safaricom Menu is under construction.")
        elif choice == "2":
            mpesa_menu()
        else:
            print("Invalid choice. Please try again.")

def mpesa_menu():
    """M-PESA menu."""
    while True:
        print("\nSIM 1 - M-PESA")
        print("1. Send Money")
        print("2. Withdraw Cash")
        print("3. Buy Airtime")
        print("4. Loans and Savings")
        print("5. Lipa na M-PESA")
        print("6. My Account")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            send_money()
        elif choice == "2":
            print("Withdraw Cash selected.")
        elif choice == "3":
            print("Buy Airtime selected.")
        elif choice == "4":
            print("Loans and Savings selected.")
        elif choice == "5":
            print("Lipa na M-PESA selected.")
        elif choice == "6":
            print("My Account selected.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def send_money():
    """Send Money submenu."""
    while True:
        phone_number = input("\nEnter Phone Number (10-13 digits): ")
        if phone_number.isdigit() and 10 <= len(phone_number) <= 13:
            amount = input("Enter amount to send: ")
            if amount.isdigit() and float(amount) > 0:
                print(f"Sending {amount} to {phone_number}.")
                break
            else:
                print("Invalid amount. Try again.")
        else:
            print("Invalid phone number. Try again.")

# Run the program
safaricom_menu()
