import re

all_total = 0
do_total = 0
is_doing = True

with open('input.txt', 'r') as f:
    s = f.read().strip()

matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", s)
for m in matches:
    if m == "do()":
        is_doing = True
    elif m == "don't()":
        is_doing = False
    else:
        a, b = re.findall(r"\d+", m)
        all_total += int(a) * int(b)
        if is_doing:
            do_total += int(a) * int(b)

print(f"All total: {all_total}")
print(f"Do total: {do_total}")
