print()
#tire_volume
import math
from datetime import datetime
current_date_and_time = datetime.now(tz=None)

    
text1 = (input("Enter the width of the tire in mm (ex 205): "))
width = float(text1)
text2 = (input("Enter the aspect ratio of the tire (ex 60): "))
aspect_ratio = float(text2)
text3 = (input("Enter the diameter of the wheel in inches (ex 15): "))
diameter = float(text3)
# calculate tire volume in liters
volume = (math.pi*width**2*aspect_ratio*(width*aspect_ratio+ 2540*diameter))/10000000000

# Open the file for appending text
with open("volumes.txt", "a") as file:
    # Write the values to the file
    file.write(f"Width: {width}")
    file.write(f"Aspect Ratio: {aspect_ratio}")
    file.write(f"Diameter: {diameter}")
    file.write(f"Volume: {volume}")
print()
# print the approximate tire volume
print(f"The approximate volume is {volume:.2f} liters")
print()
print(f"{current_date_and_time:%Y-%m-%d}, {width:.2f}, {aspect_ratio:.2f}, {diameter:.2f}, {volume:.2f}")


