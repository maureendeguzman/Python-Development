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
pi = 3.14159
height = (width * aspect_ratio / 100) / 2.80
volume = pi * (height ** 2) * (diameter / 2) * 0.001

# Open the file for appending text
with open("volumes.txt", "a") as file:
    # Write the values to the file
    file.write(f"Width: {width}\n")
    file.write(f"Aspect Ratio: {aspect_ratio}\n")
    file.write(f"Diameter: {diameter}\n")
    file.write(f"Volume: {volume}\n")
print()
print(f"{current_date_and_time:%Y-%m-%d}, {width:.2f}, {aspect_ratio:.2f}, {diameter:.2f}, {volume:.2f}")
# print the approximate tire volume
#print(f"The approximate volume is {volume:.2f} liters")

