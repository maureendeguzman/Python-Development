#Import Library
import datetime

#information

name = "Maureen Special Rice"
add = "---Dulong Ilaya---"
num = "--0953 312 2190--"
cashier = "Maxxine"
now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")

#thank you message

message = "Thank you! Come Again and Again!!"
message1 = "Mabuhay!!!"

print()
print(f"*" * 50)
print(f"\t\t{name.title()}")
print(f"\t\t{add}")
print(f"\t\t{num}")
print("=" * 50)
print(f"Cashier: {cashier}")
print(f"{date_time [0:10]}\t\t\t{date_time [10:]}")
print("=" * 50)
print("\t\t---Restaurant---")
print()

#I'm giving the restaurant a name, place and contact #.
#And some designs for the receipt(*.*)

print()
#c_meal = float(input("What is the price of a child's meal? "))
c_meal = float(input("Burger & Fries w/ Drinks "))
total_cost1 = c_meal + (c_meal * .06) + (c_meal * .15)
#a_meal = float(input("What is the price of an adult's meal? "))
a_meal = float(input("Spagetti & 1pc Chicken w/ Drinks "))
total_cost2 = a_meal + (a_meal * .06) + (a_meal * .15)

#change the menu if you want. Diffirent offer.
#change the tax_rate if you have a differnt tax rate.
#change the tip according to your generosity or services they did while doing their job.(*_*)

#children = int(input("How many children are there? "))
children = int(input("How many Burger & Fries w/ Drinks? "))
c_count = children + (children)
#adult = int(input("How many adult are there? "))
adult = int(input("How many Spagetti & 1pc Chicken w/ Drinks? "))
a_count = adult + (adult)
tax_rate = float(input("What is the sales tax rate? "))


print()
count = (c_meal * children) + (total_cost1)
count1 =(a_meal * adult) + (total_cost2)
result = (count + count1)
print (f"Subtotal: $%.2f " % result)

total = (result * .06)
print(f"Sale Tax: $%.2f " % total)
total2 = (result + total)
tip = (total_cost1 + total_cost2)
print(f"Tip: $%.2f "% tip)
print("-"*20)
total2 = (result + total)
print(f"Total: $%.2f " % total2)
print("-"*20)
print()
payment = int(input("What is the payment amount? "))
change = (payment - total2)
print(f"Change: $%.2f" %change)

print()
print("*"*50)
print()
print(f"\t{message}")
print(f"\t\t{message1}")

#I put some designs and messages to look beautifully.
#I also add some menu just change the menu if you want to try the other.
#I'm happy doing this program, I know this is just a simple one, but this program prove something.
