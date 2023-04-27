def display_regular(name):
    print(name)
    
def display_uppercase(name):
    new_name = name.upper()
    print(new_name)
    
def display_lowercase(name):
    new_name = name.lower()
    print(new_name)
    
name = input("What is your name? ")

display_regular(name)
display_uppercase(name)
display_lowercase(name)