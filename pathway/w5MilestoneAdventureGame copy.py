print()
print("~" *100)
print()
print("This GAME will help you to practice your FREEDOM to choose,")
print("BUT, you should be careful of your CHOICES...")
print()
print("(-_-)...WELCOME TO MY WORD ADVENTURE GAME...(-.-)")
print()
name = input("Enter your name!\n")
while name == "":
  print("You did't enter your name.")
  name = input("Enter your name:\n")
start = input("Do you want to play this text adventure game?[yes/no]\n")
print()
if start.capitalize() == "Yes":
 print("~"* 100) 
 print("Great! Let's play the game!")
 print()
 print(f"Greetings {name}! ")
 print("~"* 100)
else: 
  print("Restart.Try Again...")
  quit()
print("At your very young age, you inherit the old mansion of your grandmother,")
print("as a hiers you need to pay a visit and check your old mansion.")
print("Now your on your way to the old mansion.")
print()
setting = input("At your arrival, you notice that the door is already open, are GOING inside or Stay outside?[GOING/STAY]\n")
print()
if setting.capitalize() == "Going":
  print("You are now inside the Mansion, and its very dark and creepy. Oh nooo!")
  response1 = input("You look around and you saw a MATCH and candle to give light or just open the WINDOWS and curtains?[MATCH/WINDOWS]\n")
  
  if response1.capitalize() == "Match":
    print("You light up the candle by match but, its still dark in some part of the mansion!")
    response2 = input("Are you KEEP going or LEAVE the mansion? And plan a visit some other day.[KEEP/LEAVE]\n")
    
    if response2.capitalize() == "Keep":
      print("Because of the candle, it only provide a little light and you din't notice the snake crawling and its coming to you. The snake bit you. Sorry you lose")
    elif response2.capitalize() == "Leave":
      print("You decide to retun another day with someone, its more safe. Congratulation! You did a great decision.")
    else:
      print("invalid option, you lose!")
  
  elif response1.capitalize() == "Windows":
    print("Wow! Now you see everything inside the mansion! Its full of antique furnitures but it's very dirty")
    response3 = input("What are you going to do now? YOU will start cleaning or call ANYONE can do the cleaning? A house cleaner service.[YOU/ANYONE\n")
    
    if response3.capitalize() == "You":
      print("I can't do this alaone. It's very tiring! You can't do it alone. Not a good decision. You lose!")
    elif response3.capitalize() == "Anyone":
      print("Wow! We made it! We clean the mansion in no time. And it's looked amazing. Congratulation! You did a great job!")
    else:
      print("Invalid option, you lose!(T.T)")
  
  else:
    print("Invalid option, you lose!(T.T)")
     
elif setting.capitalize() == "Stay":
  print("OMG! What should I do now, I don't want to go inside, because this place is not familiar to me.")
  response1 = input("Do i need to call my FRIEND to help me or go HOME and try again some other time.[FRIEND/HOME]\n")
  
  if response1.capitalize() == "Friend":
    print("Can you come over and help me to check the mansion. ASAP('.').")
    response5 = input("While waiting out side you heard a sound inside the Mansion. Are you going to LOOK for it or IGNORE it?[LOOK/IGNORE]\n")
    
    if response5.capitalize() == "Look":
      print("You become more fearful and don't want to check the mansion. I'm going o sell it! Not a good decision. You disappoint your Grandma. You lose!")
    elif response5.capitalize() == "Ignore":
      print("I will wait for my friend to check it out later, so I will know what to do next. You are so smart. Congratulation! Your Grandma is so proudbof you!")
    else:
      print("Invalid option, you lose!(T.T)")
  
  elif response1.capitalize() == "Home":
    print("I think I'm more safe here in my apartment") 
    response6 = input("Now I think I will SELL the mansion or GIVE to my parents.[SELL/GIVE]\n")
    
    if response6.capitalize() == "Sell":
      print("Oh no! Your gradmother will be mad at you. Very poor decision! You lose!")
    elif response6.capitalize() == "Give":
      print("Good job! Giving is caring! They have more time to take good care of the mansion. Congratulation!")
    else:
     print("Invalid option, you lose!(T.T)")
  
  else: 
   print("Invalid option, you lose!(T.T)")

else:
  print("Invalid option, you lose!(T.T)")
print("~"* 100)
print("(-.-)Thank you for playing! Goodbye.('.')")
print("~" * 100)
print()
rate = int(input("Rate my Game (from 1-10) 1 is the lowes and 10 is the highest.\n"))
if rate >= 5:
  print(f"Your Rate is ( {rate} ) Thank you! Your AWESOME!!!")
else:
  print(f"Your Rate is ( {rate} ) Thank you! I will continue improving my Word Adventure Game.")
print("~" * 100)
print("===========================================PLAY AGAIN!!==========================================")
print("~"* 100)

# I design it with ~ line
# I use loops in line 10, its simple but trying to learn.
# I thingk I exceeded the requirments
# I let my husband and friends play my games, and they told me that I MADE A GREAT JOB! In this project. 
