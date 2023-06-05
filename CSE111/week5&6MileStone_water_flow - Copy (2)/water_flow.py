import math

def water_column_height(tower_height, tank_height):
    tower_height = str(tower_height)
    tank_height = str(tank_height)
   
    water_height = tower_height  + (str(3) * tank_height / str(4))
    
    return water_height

def pressure_gain_from_water_height(height):
    height = (height)
    p = float(998.2)
    g = float(9.80665)
    
    pressure_gain = float(p) * float(g) * float(height) / 1000
    return pressure_gain

def pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity):
    friction_factor = 0.02
    pipe_length = 100  
    density_water = 998.2  
    fluid_velocity = 5  
    pipe_diameter = 0.2  
    
    pressure_loss = (-friction_factor * pipe_length * density_water * fluid_velocity * 2 * 2) / (2000 * pipe_diameter)
    
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    water_density = 998.2
    fluid_velocity = ""
    quantity_fittings = ""
    

    pressure = -0.04 * water_density * fluid_velocity * fluid_velocity * quantity_fittings /2000

    return pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    hydraulic_diameter = ""
    fluid_velocity = ""

    raynolds = 998.2 * hydraulic_diameter * fluid_velocity / 0.0010016

    return raynolds

def pressure_loss_from_pipe_reduction(larger_diameter,fluid_velocity, reynolds_number, smaller_diameter):
    
    reynolds_number = ""
    large_diameter = ""
    smaller_diameter = ""
    water_density = 998.2
    larger_diameter = ""

    k = (reynolds_number * smaller_diameter) / large_diameter
    P = 0.5 * water_density * fluid_velocity**2 * (1 - (smaller_diameter**4 / larger_diameter**4)) * k
    
    return P

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()



