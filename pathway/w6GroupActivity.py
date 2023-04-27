print()
print()
first_rider_age = int(input("What is the age of the first rider? "))

height = int(input("What is the height of the first rider? "))
rider = str(input("Is there a second rider(yes/no)? "))
if rider.capitalize() =="yes":
    should_ride = True
elif rider.capitalize() =="No": 
    should_ride = False
    print("Sorry, you may not ride.") 
    quit()
second_rider_age = int(input("What is the age of second rider? "))
h_s_rider =int(input("What is the height of the second rider? "))

if first_rider_age or second_rider_age >= 50:
    should_ride = False
    print("Sorry, you may not ride.")
    if height >= 62 and first_rider_age >= 18:
        should_ride = True
    elif height <= 62 and first_rider_age <= 18:
        if first_rider_age <= 18: 
            should_ride = False
        else:
            should_ride = False
    else:
        should_ride = False
elif first_rider_age or second_rider_age>= 18:
    should_ride = True        
else:
    if first_rider_age or second_rider_age >=50:
        should_ride = False
    elif second_rider_age <= 18:
        should_ride = True
    else:
       if height >= 62 and second_rider_age >= 18:
           should_ride = True
       elif height <= 62 and second_rider_age <= 18:
           should_ride = False
       else:
           should_ride = False
           if should_ride:
             print("Welcome to the ride. Please be safe and have fun!") 
           else:
             print("Sorry, you may not ride.") 
    
                  
        
        
        