

print("*"*20, "Welcome To SBI ATM", "*"*20)         # Prints a welcome message with decorative asterisks
amt = 20000.0           # Sets the initial account balance
pin = 454545            # Defines a predefined PIN for the ATM
cart = input("Insert card y/n:  ").lower()          # Prompts the user to insert the card and converts input to lowercase

if cart == "y":                # Checks if the user has inserted the card
    lang = input("Select language:\n\t1. Hindi\n\t2. English\n")          # Prompts the user to select a language
    if lang == "1" or lang == "2":           # Validates the language selection
        acc = input("Select account type\n\t1. Saving\n\t2. Current\n")         # Prompts the user to select the account type
        if acc == "1":           # Checks if the user has selected the 'Saving' account type
            p = int(input("Enter your pin: "))         # Prompts the user to enter their PIN
            if p == pin:                   # Validates the entered PIN
                while True:                 # Starts an infinite loop for ATM operations
                    opr = int(input("Select operation:\n\t1. Check balance\n\t2. Withdrawal\n\t3. Deposit\n"))  # Prompts the user to select an operation
                    if opr == 1:            # Checks if the user selected 'Check balance'
                        print("Your account balance is: ", amt)             # Prints the current account balance
                    elif opr == 2:               # Checks if the user selected 'Withdrawal'
                        b = float(input("Enter amount to withdraw: "))                 # Prompts the user to enter the amount to withdraw
                        if b <= amt:                 # Checks if the account has sufficient balance
                            amt -= b                 # Deducts the withdrawal amount from the account balance
                            print("Your current balance is: ", amt)                      # Prints the updated account balance
                        else:
                            print("Insufficient balance")                     # Prints an error message if the balance is insufficient
                    elif opr == 3:                        # Checks if the user selected 'Deposit'
                        a = float(input("Enter amount to deposit: "))                  # Prompts the user to enter the amount to deposit
                        amt += a                        # Adds the deposit amount to the account balance
                        print("Your current balance is:  ", amt)                          # Prints the updated account balance
                    else:
                        print("Invalid operation")                         # Prints an error message for an invalid operation selection
                        
                    ex = input("Do you want to exit? y/n: ").lower()                 # Prompts the user to decide whether to exit
                    if ex == "y":                        # Checks if the user wants to exit
                        break                 # Exits the loop if the user chooses to exit
            else:
                print("Invalid PIN")                            # Prints an error message if the entered PIN is incorrect
        else:
            print("Please select a valid account type")                # Prints an error message if the selected account type is invalid
    else: 
        print("Please select a valid language")                        # Prints an error message if the selected language is invalid
else:
    print("Invalid card")                          # Prints an error message if the card is not inserted correctly
