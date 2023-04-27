import math
print()
n = int(input("Enter the number of items: "))
n_i = int(input("Enter the number of item per box: "))
print()
n_b = math.ceil(n/n_i)
print(f"For {n} items, packing {n_i} items in each box, you will need {n_b} boxes.  ")