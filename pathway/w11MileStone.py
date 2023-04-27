import csv

max_life_expectancy = -1
min_life_expectancy = 9999
average = -1
year_count = -1
country_max = ""
country_min = ""
year_max = ""
year_min = ""
high_value = 0
low_value = 99
country_high = ""
country_low = ""
life = []



with open("life-expectancy.csv", 'r') as csv_life:
    csv_reader = csv.reader(csv_life)
    next(csv_reader)
# I open and manage the files
    
    for line in csv_life:
        new_line = line.strip()
        part = line.split(",")
        country = part[0].strip()
        year = line.split()
        years = int(part[2])
        life_expectancy = float(part[3])
        life.append(part[3])
# I divide it, I think I did it right.
        
        
        if life_expectancy >= max_life_expectancy:
                max_life_expectancy = life_expectancy
                year_max = years
                country_max = country 
                
        elif life_expectancy <= min_life_expectancy:
                min_life_expectancy = life_expectancy
                year_min = years
                country_min = country
                
        elif life_expectancy > high_value:
                high_value = life_expectancy
                year = high_value  
                country_high = country
                
        elif life_expectancy < low_value:
                low_value = life_expectancy
                year = low_value
                country_low = country
                
                
                
sum = 0
sum += life_expectancy
year = len(year)
average = sum / year



 
print()
year = int(input("Enter the year of interest: "))
print()
print(f"The overall max life expectancy is: {max_life_expectancy} from {country_max} in {year_max}")
print(f"The overall min life expectancy is: {min_life_expectancy} from {country_min} in {year_min}")
print()
# I did the first part of the program.

print(f"For the year {year}:")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was in {country_high} with {high_value:.2f}")
print(f"The min life expectancy was in {country_low} with {low_value}")
print()
# My average and high and low value is not working properly I tried so hard but I can't still figure it out.
# Until the last hour I'm trying to figure it out, I try the ChatGPT the code are not working with my program.
# I will try again this week.
country = input("Country you want to know the data of expectancy ")
expectancy = -1
year = ""
country = ""

with open("life-expectancy.csv", 'r') as csv_life:
    csv_reader = csv.reader(csv_life)
    next(csv_reader)

    for line in csv_life:
        parts = line.split(",")
        countrys = parts[0].strip()
        years = int(parts[2])
        expectancy = float(parts[3])
    
        if expectancy in csv_life:
            expectancy = expectancy
            year = year
            country = country
            
    print(f"Country with the most life ecpectancy: {countrys} Year: {years} Expectancy: {expectancy}.")   
    # I try to do additional requirements but still not working properly.
                
               