#Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space

import re

numbers = []

while True:
    string = input()
    if string == '':
        break

    pattern = r'\d+'
    matches = re.findall(pattern, string)
    numbers.extend(matches)


print(" ".join(numbers))

