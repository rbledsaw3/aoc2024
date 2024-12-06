import re
from collections import defaultdict, deque

def nums(s):
    return list(map(int, re.findall(r"-?\d+", s)))

with open("input.txt") as f:
    s = f.read().strip()

s_1, s_2 = s.split("\n\n")


results = []
for line in s_1.split("\n"):
    a, b = nums(line)
    results.append((a, b))


def is_ordered(n):
    return not any(a in n and b in n and n.index(a) > n.index(b) for a, b in results)


ans = 0
updates = [nums(update) for update in s_2.split("\n")]
correct_updates = []

for update in updates:
    if is_ordered(update):
        correct_updates.append(update)
        ans += update[len(update) // 2]

print(f"Part 1: {ans}")


def topological_sort(update, rules):
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)

    for a, b in rules:
        if a in update and b in update:
            adj_list[a].append(b)
            in_degree[b] += 1

    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) != len(update):
        raise ValueError("Cycle detected or missing nodes in topological sort.")

    return sorted_order

ans = 0
for update in updates:
    if not is_ordered(update):
        fixed_order = topological_sort(update, results)
        ans += fixed_order[len(fixed_order) // 2]

print(f"Part 2: {ans}")

