#Purpose: Practice using numbers in lists.


# Please note: For this program especially, there are MANY ways to accomplish the task.
# The following shows one way it can be done, but it's not the only way. In particular, many
# of these tasks can be done with built-in functions (such as max(numbers)), but this
# approach highlights how to compute those values directly using loops.

print("Enter a list of numbers, type 0 when finished.")

numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

# The list "numbers" now has all the numbers the user typed

# Step 1: Find the sum or total
sum = 0

for number in numbers:
    sum += number

print(f"The sum is: {sum}")

# Step 2: Find the average
# We can use the sum we just computed...
count = len(numbers)
average = sum / count

print(f"The average is: {average}")

# Step 3: Find the max
# We will walk through the numbers again, this time keeping track
# of the best so far, or the highest number to that point.

best_so_far = -1

for number in numbers:
    # Check if this number is larger than the best one we have seen so far
    if number > best_so_far:
        # This is the new best number, so save it to that variable
        best_so_far = number


print(f"The largest number is: {best_so_far}")
