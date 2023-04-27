print()
print()



numbers = []
number = -1
sum = 0
average = 0
count = 0

print("Enter a list of numbers, type 0 when finished.")
while number != 0:
    number = int(input("Enter number: "))
    numbers.append(number)
    sum += number
    
print(f"The sum is: {sum}")

count = len(numbers)
average = (sum / count)
 
print(f"The Average is: {average}")




    