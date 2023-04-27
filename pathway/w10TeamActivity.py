print()
print()
print("Enter the names and balance of bank accounts (type: quit when done)")
accounts = []
balances = []
account = None

while account != "quit":
    account = input("What is the name of this account? ")
    if account != "quit":
        balance = float(input("What is the balance? "))
        
        accounts.append(account)
        balances.append(balance)
    else:
        accounts == 0      
        
total = 0
print("\nAccount Information:")
for i in range(len(accounts)):
    print(f"{accounts[i]} - ${balances[i]}")
    total += balances[i]
    
average = total / len(balances)
print(f"Total: ${total:.2f}")
print(f"The Average is: ${average:.2f}")
    
