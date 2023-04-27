import math

def compute_area_square(side):
    """
    Computes the area of a square given its side length.
    """
    return side ** 2

def compute_area_rectangle(length, width):
    """
    Computes the area of a rectangle given its length and width.
    """
    return length * width

def compute_area_circle(radius):
    """
    Computes the area of a circle given its radius.
    """
    return math.pi * radius ** 2


while True:
    print()
    shape = input("What kind of shape do you have? (square, rectangle, circle, quit): ")

    if shape == "square":
        side = float(input("Enter the length of a side: "))
        area = compute_area_square(side)
        print(f"The area of the square is {area}")

    elif shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = compute_area_rectangle(length, width)
        print(f"The area of the rectangle is {area}")

    elif shape == "circle":
        radius = float(input("Enter the radius: "))
        area = compute_area_circle(radius)
        print(f"The area of the circle is {area}")

    elif shape == "quit":
        break

    else:
        print("Invalid input, please try again.")