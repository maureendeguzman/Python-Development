import random
shopping_cart = []
prices = []


print()
print()
print("Welcome to the Shopping Cart Program!")
print()
print("Please select one of the following:")

action = 0
while action != 5:
     print("1. Add item") 
     print("2. View Cart")
     print("3. Remove Item")
     print("4. Compute Total")
     print("5. Quit")
     if action != 5:  
          action = int(input("Please enter an action: "))
          
          if action == 1:
               item = input("What item would you like to add? ")
               price = float(input(f"What is the price of {item}? "))
               print(f"'{item}' has been added to the cart.")
               print()
               shopping_cart.append(item)
               prices.append(price)
                    
          elif action == 2:
               print("The content of the shopping cart are: ")
              
               print()
               print("~"*100)
               print("Number\t\tQuantity\tItem\t\tPrice")
               print("~"*100)
               for i in range(len(shopping_cart)):
                    item = shopping_cart[i]
                    price = prices[i]
                    print(f"  {i +1}.\t\t  {shopping_cart.count(item)}x\t\t{item }\t\t ${price:.2f}")
               print("~"*100)    
                    #the quantity is working but it will print again, the variable and the price i dont know how to fix it.
          elif action == 3:
               i = -1
               remove = int(input("Which item would you like to remove? "))
               shopping_cart.pop(i -1)
               prices.pop(i -1)
               print("Item remove")
               print("Plase select the following:")
               #when you remove a variable at first it will work properly
               #but if you will add again after you remove, and remove again it will not work properly
          elif action == 4:
               sum = 0
               for price in prices:
                    sum += price
               print()
               print(f"Total price of the items in the shopping cart is ${sum:.2f}")
               quit
          else:
               quit
               
else:
     print("Thank you. Goodbye")
#for the creativity and exeeding requirments
#I add alingment for quantity items and price.
#but the quantity didn't work. I don't know how ti fix it.