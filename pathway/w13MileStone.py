def wind_chill(temp, wind_speed):
    
    if wind_speed < 3 or temp > 50:
        # Formula not applicable
        return temp
    wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp * (wind_speed ** 0.16))
    return wind_chill


def celsius_to_fahrenheit(temp_celsius):
    
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit
def fahrenheit_to_celsius(temp_fahrenheit):
    
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    return temp_celsius

print()
temp = float(input("What is the temperature? "))
scale = input("Fahrenheit or Celsius (F/C)? ")

if scale.lower() == 'c':
    temp = (temp * 9/5) + 32


for wind_speed in range(5, 65, 5):
    wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp * (wind_speed ** 0.16))
    
    if scale.lower() == 'c':
        wind_chill = (wind_chill - 32) * 5/9 
        print("At temperature {0:.1f}F, and wind speed {1} mph, the windchill is: {2:.2f}C".format(temp, wind_speed, wind_chill))
    else:
        print("At temperature {0:.1f}F, and wind speed {1} mph, the windchill is: {2:.2f}F".format(temp, wind_speed, wind_chill))
        
        
        