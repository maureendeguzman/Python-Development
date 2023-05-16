import math

def main ():
    max_storage_efficiency= max_cost_efficiency=0
    cans=[
    ["Name", "Radius (cm)", "Height (cm)", "Cost per Can (US$)"], \
    ["#1 Picnic", 6.83, 10.16, 0.28], \
    ["#1 Tall", 7.78, 11.91, 0.43], \
    ["#2", 8.73, 11.59, 0.45], \
    ["#2.5", 10.32, 11.91, 0.61], \
    ["#3 Cylinder", 10.79, 17.78, 0.86], \
    ["#5", 13.02, 14.29, 0.83], \
    ["#6Z", 5.40, 8.89, 0.22], \
    ["#8Z short", 6.83, 7.62, 0.26], \
    ["#10", 15.72, 17.78, 1.53], \
    ["#211", 6.83, 12.38, 0.34], \
    ["#300", 7.62, 11.27, 0.38], \
    ["#303", 8.10, 11.11, 0.42] \
    ]
    best_storage=0
    best_storage_can=None
    best_cost=0
    best_cost_can=None

    for number, line in enumerate (cans):
        if number:
            name= line[0]
            radius= line[1]
            height= line[2]
            cost_per_can= line[3]
            #volume= compute_volume(radius, height)
            #surface_area= compute_surface_area(radius, height)
            storage_efficiency= compute_storage_efficiency(radius, height)
            cost_efficiency= compute_cost_efficiency(cost_per_can,radius,height)
            if storage_efficiency > best_storage:
                best_storage = storage_efficiency
                best_storage_can = number
            if cost_efficiency > best_cost:
                best_cost = cost_efficiency
                best_cost_can = number 
            print(f"{name}, {storage_efficiency:.2f}, {cost_efficiency:.2f}")
    print(f"The can with the best efficiency:{cans[best_storage_can][0]}")
    print(f"The can with the best cost: {cans[best_cost_can][0]}")

def compute_volume(radius, height):
    volume= math.pi*(radius**2)*height
    return volume
    
def compute_surface_area(radius, height):
    surface_area= 2*math.pi*radius*(radius + height)
    return surface_area
def compute_storage_efficiency(radius, height):
    volume= compute_volume(radius, height)
    surface_area= compute_surface_area(radius, height)
    storage_efficiency= volume / surface_area
    return storage_efficiency
def compute_cost_efficiency(cost_per_can, radius, height):
    volume= compute_volume(radius, height)
    cost_efficiency= volume / cost_per_can
    return cost_efficiency
main()

#1 Picnic 2.04
#1 Tall 2.35
#2 2.49
#2.5 2.76
#3 Cylinder 3.36
#5 3.41
#6Z 1.68
#8Z short 1.80
#10 4.17
#211 2.20
#300 2.27
#303 2.34