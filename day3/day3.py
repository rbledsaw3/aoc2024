import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

total = 0

with open('input.txt', 'r') as f:
    for line in f:
        matches = re.findall(pattern, line)
        for x, y in matches:
            total += int(x) * int(y)

print(total)
