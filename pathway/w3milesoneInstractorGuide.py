#Areas of shapes

#square 
side = float(input("What is the lengtht of a side of the square? "))
area = side **2
print(f"The area of square is: {area}")

#rectangle
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
ares = length*width
print(f"the area of rectangle is: {area} ")

#circle
radius = float(input("What is the radius of the circle? "))
area = 3.14* (radius**2)
print(f"The area of the circle is: {area}")

#stretch 1 using the math library
import math
radius = float(input("What is the radius of the circle? "))
area = math.pi* (radius**2)
print(f"The area of the circle is: {area}")

#Stretch 2 Many areas from one value
value = float(input("What is the value to be use?"))

#calculate areas
ares_square = value **2
area_circle = math.pi *(value **2)
volume_cube = value **3
volume_sphere = (4/3)* math.pi*(value**3)

#display results
print(f"Area of a square: {ares_square} ")
print(f"Area of a circle: {area_circle} ")
print(f"Volume of a cube: {volume_cube} ")
print(f"Volume of a square: {volume_sphere} ")

#stretch 3: cm-> m conversion
#For this stretch challenge, the code above could simply be updated, but it is
#duplicated here so that the above code is not cofusing when it is viewed.

#area of square
side = float(input("What is the length of the side of a square(in cm)? "))
ares = side **2

print(f"The area of the square is: {area} cm^2")

#In the above example, the area was computed first and saved into a variable,
#but the code for computation can also be put right into the print statement
#if you would rather do that. In the next example, the computer is 
#included right in the print statement.
#also, please note that you do not put commas in numbers in code(use:10000, not 10,000)
print(f"The area of the square is: {area/10000 m^2")

#area of rectangle
length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of rectangle (in cm)? "))
area = length*width
print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of rectangle is: {area/10000} m^2 ")

#area of a circle
radius = float(input("Wha is the radius of the circle(in cm)? "))
area = 3.14* (radius **2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area/10000} m^2")