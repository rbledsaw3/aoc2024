safe = 0

with open("input.txt") as f:
    for l in f:
        line = [int(num) for num in l.split()]
        isSameDirection = True
        isIncreasing = line[1] > line[0]
        for i in range(len(line) - 1):
            diff = line[i + 1] - line[i]
            if abs(diff) < 1 or abs(diff) > 3:
                isSameDirection = False
                break
            if (diff > 0) != isIncreasing:
                isSameDirection = False
                break
        if isSameDirection:
            safe += 1
print(safe)
