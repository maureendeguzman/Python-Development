from datetime import datetime, timedelta

print()
sub_total = float(input("Please enter the subtotal: "))
total_cost = sub_total * .06
total = sub_total + total_cost
discount = total - .10
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

print(day_of_week)
print(f"Discount amount: {discount}")
print(f"Sale tax amount: {total_cost:.2f}")
print(f"Total: {total:.2f}")