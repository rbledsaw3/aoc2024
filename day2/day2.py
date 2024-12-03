def is_safe(line):
    isIncreasing = line[1] > line[0]
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if (diff > 0) != isIncreasing:
            return False
    return True

def is_safe_with_dampener(line):
    for i in range(len(line)):
        mod_line = line[:i] + line[i + 1:]
        if len(mod_line) >= 2 and is_safe(mod_line):
            return True
    return False

safe = 0

with open("input.txt") as f:
    for l in f:
        line = [int(num) for num in l.split()]
        if is_safe(line) or is_safe_with_dampener(line):
            safe += 1
print(safe)
