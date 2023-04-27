# Grading system in Python
# ("A = 90")
# ("B = 80")
# ("C = 70")
# ("D = 60")
# ("F = 60")

print()
#grade = int(input("Your Marks is: "))
grade = float(input("Your Marks is: "))
#you can change if it's not a whole #
if grade >= 90:
    G_letter = ("A")
elif grade >= 80:
    G_letter = ("B")    
elif grade >= 70:
    G_letter = ("C")
elif grade >= 60:   
    G_letter = ("D")
elif grade < 60:
    G_letter = ("F")

# Another condition with + or -
G_sign =  grade % 10
if G_sign >= 7 and G_letter in('A' , 'F'):
    print(G_letter)
elif G_sign <= 7 and G_letter == 'F':
    print(G_letter)    
elif grade >= 7:
    print(G_letter + '+')
else:  
    print( + "-")
    
# Stretch Challenge 2
if grade >= 93:
    G_sign = ""
    
# Stertch Challenge 3
if G_letter >= "F":
    G_sign = ""    
print(f"Your mark i: {G_letter}{G_sign}")
 
if grade >= 70:
    print("Congratulation! You passed the class!")
else: 
    print("Stay focus and you'll get it next time!")
print()         
