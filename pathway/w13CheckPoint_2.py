def display_first(message):
        regular = message
        print(regular)
def display_second(message):
    s = message.upper()
    print(s)
def display_third(message):
    t =  message.lower()
    print(t)      
    
message = input("What is your massage? ")

display_first(message)
display_second(message)
display_third(message)
