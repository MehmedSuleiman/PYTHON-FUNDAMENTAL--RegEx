#Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".
# The price could be a floating-point or integer number.
# You should store the names of the furniture and the total price.
#In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
#"Bought furniture:
#{1st name}
#{2nd name}
#…
#{N name}
#Total money spend: {total_cost}"


import re

furnitures = []
total_cost = 0

while True:
    furniture = input()
    if furniture == 'Purchase':
        break

    pattern = r'([>>]+)([A-Za-z]+)([<<]+)([0-9].*)([!])([0-9]+)'
    matches = re.finditer(pattern, furniture)

    for match in matches:
        furniture, cost , quantity = match[2], float(match[4]), int(match[6])
        total_cost += cost*quantity
        furnitures.append(furniture)

print("Bought furniture:")
for furniture in furnitures:
    print(furniture)

print(f"Total money spend: {total_cost:.2f}")
