# Looping through list
items = ["crayon","scissor","paper","glitter glue","markers","pen"]
for item in items:
   print(f"The item is:{item}")

#Looping through numbers
#number = range(5)
#for i in range(5):
#   print(i)
#   for j in range(10,13):
#     print(f"--{j}")
#While we generally prefer variable names that are more descriptive than a single letter, if the variable will only be used for counting in a simple loop it is considered standard to use i. Then, if you have an inner loop, you use j, and a third inner loop would be k. If you have more than three loops you should consider if there is a simpler way to accomplish your task, and if there really isn't, you should at least move to more descriptive variable names at that point.


#looping through string
#first_name = "Brigham"
#for letter in first_name[3]:
#   print(f"The letter is: {letter}")

#iterating through each letter using an index
#word = "book"
#number_of_letter = 4

#for index in range(number_of_letter):
#   letter = word[index]
#   print(f"index: {index} Letter: {letter}")

#finding the string length
#dog_name = input("What is your dog name? ")
#letter_count = len(dog_name)

#print(f"Your dog's name has {letter_count} letters")

#first_name = "Brigham"

# Notice by using enumerate, we specify both i and letter
#for i, letter in enumerate(first_name):
#    print(f"The letter {letter} is at position {i}")