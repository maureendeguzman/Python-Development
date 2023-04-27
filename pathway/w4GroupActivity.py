
print(f"Welcome to the velocity calculator. Please enter the following: ")
print()
mass = float(input("Mass (in kg):" ))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds: "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross = float(input("Cross sectional area (in m^2): "))
constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

print()
import math
value = (1/2) * density * cross * constant
velocity = math.sqrt(mass * gravity / constant) * (1 - math.exp((-math.sqrt(mass * gravity * constant) / mass) * time))
print(f"The inner value of c is:{value:.3f} ")
print(f"The velocity after 10.0 second is: {velocity:.3f} m/s")