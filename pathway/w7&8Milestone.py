import random
print()
print()

name = input("Enter your name!\n")
while name == "":
  print("You did't enter your name.")
  name = input("Enter your name:\n")
start = input("Do you want to play Word Guessing game?[yes/no]\n")
print()
if start.capitalize() == "Yes":
 print("Great! Let's play the game!")
 print(f"Greetings {name}! ")
else: 
  print("Restart.Try Again...")
  quit()
print()
print("="* 100)
print(f"\t\t\t\tWELCOME TO THE WORD GUESSING GAME!")
print(f"\t\t\t\t\tEnjoy, and have fun!!!")
print("="*100)
secret_word = "PRIESTHOOD".capitalize()
display = "_ "* len(secret_word.capitalize())
count = 0
user_guess = ""
letter = ""

keep_playing = "yes"
print(f"Your hint is: " + display)
user_guess = input("What is your guess? ")
if user_guess != secret_word:
      print(f"Sorry, the guess must the same number of letter as the secret word.")
while keep_playing == "yes":
  count = 0 
  
  while user_guess != secret_word:
    
    user_guess = input("\nWhat is your guess? ")
    
    if user_guess != secret_word:
      print(f"Sorry, the guess must the same number of letter as the secret word.")
      
      
      for i,letter in enumerate(secret_word):
        
        if (secret_word[i].lower() == secret_word.lower()):
          print(user_guess[i].upper(), end=" ")
        
        elif (user_guess[i].lower() in secret_word):
          print(user_guess[i].lower(), end=" ")
          
        else:
          print("_", end= " ")
          
          count = count + 1
     
    else:
      print("Congratulation! You guessed it!")
      
      print(f"It took you {count} guesses.")
      

