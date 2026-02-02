correct_pin = "miz2007"
attempts = 3
balance = 50000

while attempts > 0:
    user_pin = input("Enter your ATM PIN: ").strip()

    if user_pin == correct_pin:
        print("Login Successful ✅")

        # ATM MENU
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")

        while True:
            choice = input("Enter your choice 1, 2 or 3: ")

            if choice == "1":
                print("Your Current Balance is:", balance)

            elif choice == "2":
                amount = int(input("Enter amount to withdraw: "))

                if amount > balance:
                    print("Insufficient Balance ❌")
                else:
                    balance -= amount
                    print("Please collect your cash 💵")
                    print("Current Balance:", balance)

            elif choice == "3":
                print("Thank you for using ATM 👋")
                break

            else:
                print("Invalid Option ❌")

        break

    else:
        attempts -= 1
        print("Wrong PIN ❌")
        print("Attempts left:", attempts)

        if attempts == 0:
            print("Account Blocked 🚫")






