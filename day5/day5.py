import re
from collections import defaultdict

def nums(s):
    match = re.findall(r"-?\d+", s)
    return [int(x) for x in match]

with open("input.txt") as f:
    s = f.read().strip()

s_1, s_2 = s.split("\n\n")

results = []
ans = 0

for line in s_1.split("\n"):
    a, b = nums(line)
    results.append((a, b))

c = {}

for x in s_2.split("\n"):
    n = nums(x)
    good = not any(
        a in n and b in n and n.index(a) > n.index(b) for a, b in results
    )
    if good:
        ans += n[len(n) // 2]

print(ans)


