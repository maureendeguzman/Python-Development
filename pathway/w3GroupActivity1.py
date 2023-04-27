#Purpose: Areas of shapes 

# Area ofsquare
lenghth = int(input("What is the lenghth of a side of the square(cm)? "))
area = lenghth**2/10000
print(f"The area of the square is: "+ str(area) +"(m2)")

#Area of rectangele
lenghth2 = float(input("What is the lenghth of the rectangle(cm)? "))
width = float(input("What is the width of the rectangle (cm)? "))
area2 = lenghth2*width
print(f"The area of rectangle is: " + str(area2) + "(m2)")

#Area of circle
import math
radius = float(input("What is the radius of the circle(cm) ?"))
area3 = radius*radius*math.pi/10000
print(f"The area of the circle is: " + str(area3)+ "(m2)" )

