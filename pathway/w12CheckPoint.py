people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
people_age = 9999
people_name = ""
for person in people:
    parts = person.split()
    name = parts[0]
    age = int(parts[1])
    
    if age > people_age:
        people_age = age
        
        people_name = name
print(f"The youngest is: {age}")
print(f"The youngest name is: {name}")