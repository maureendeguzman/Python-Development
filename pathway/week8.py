word = "commitment"

favorite_letter = input("What is your favorite letter? ")

###
# Core Requirements #1 and #2
###
for letter in word:
    # Just in case the word or the user's letter contain a capital, we
    # should convert the letters to lowercase when we compare them
    if letter.lower() == favorite_letter.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

###
# Core Requirement #3
###
for letter in word:
    # Just in case the word or the user's letter contain a capital, we
    # should convert the letters to lowercase when we compare them
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()

#Purpose: Capitalizes letters in a string. Including the stretch challenges.
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

run_again = "yes"

while run_again == "yes":
    user_number = int(input("Please enter a number: "))

    for i, letter in enumerate(quote):
        # Remember that the % operator divides by a number and returns the remainder.
        # So we can get every 3rd letter by dividing by 3 and looking for a remainder of 0,
        # or more generically, we can divide by the user's number
        if i % user_number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    
    # This puts a newline at the end of the list of quote
    print()

    run_again = input("Would you like to enter another number? ")

print("Goodbye")