import csv
print()
year = int(input("Enter the year of interest: "))


max_life_expectancy = -1
min_life_expectancy = -1
high_value = ""
low_value = ""
average = 0
with open("life-expectancy.csv" , "r") as csv_life:
    csv_reader = csv.reader(csv_life)
    next(csv_reader)


    for line in csv_life:
        parts = line.split(",")
        country = parts[0].strip()
        years = int(parts[2])
        life_expectancy = float(parts[3])
        
        if max_life_expectancy == year:
                  

    
            if years > max_life_expectancy:
                max_life_expectancy = years
                high_value = country 
print(f"The overall max life expectancy is: {max_life_expectancy} from {country} in {years}")
print(f"The overall min life expectancy is: {min_life_expectancy} from {country} in {years}")
print(f"The max life expectancy was in {country} with {high_value}")
print(f"The min life expectancy was in {country} with {low_value}")
