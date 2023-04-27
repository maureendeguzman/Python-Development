#with open("hr_system.txt") as hr_file:
#     for line in hr_file:
#         new_line = line.strip()
##         parts = line.split(" ")
         
#         name = parts[0]
#         title = parts[2]
#         print(f"Name: {name},\tTitle: {title} ")



with open("hr_system.txt") as hr_file:
    for line in hr_file:
        clean_line = line.strip()
        parts = clean_line.split(" ")
         
        name = parts[0]
        id_number = parts[1]
        title = parts[2]
        salary = float(parts[3])
         
        pay_amount = salary / 24
         
        if title.lower() == "engineer":
            pay_amount += 1000
        print(f"{name} (ID:{id_number}), {title} - ${salary:.2f}")