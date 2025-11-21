#Write a program that finds all variable names in each string.
# A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits.
# Extract only their names without the underscore. Try to do this only with regular expressions.
#he output consists of all variable names extracted and printed on a single line, separated by a comma.

import re

def is_valid_name(name):
    pattern = r"^_([a-zA-Z0-9]+)"
    match = re.findall(pattern, name)
    return match

names = input().split()
valid_names = [name for name in names if is_valid_name(name)]
names_without_underscore = []
for name in valid_names:
    if name[0] == "_":
        names_without_underscore.append(name[1:])


print(",".join(names_without_underscore))

