with open('input.txt') as f:
    s = f.read().strip()

ans = 0

adj8 = [(0, 1), (1, 0), (0, -1), (-1, 0),
        (1, 1), (-1, -1), (1, -1), (-1, 1)]

grid = [list(row) for row in s.split('\n')]
h, w = len(grid), len(grid[0])

for i in range(h):
    for j in range(w):
        for dx, dy in adj8:
            cx, cy = i, j
            result = ""
            for _ in range(4):
                if cx not in range(h) or cy not in range(w):
                    break
                result += grid[cx][cy]
                cx += dx
                cy += dy
            if result == "XMAS":
                ans += 1

print(f"Answer to part 1: {ans}")
ans = 0

for i in range(1, h - 1):
    for j in range(1, w - 1):
        if grid[i][j] == 'A':
            for dx, dy in adj8:
                if dx == 0 or dy == 0:
                    continue
                if grid[i + dx][j + dy] == 'M' and grid[i - dx][j - dy] == 'S' \
                        and ((grid[i - dy][j + dx] == "M" and grid[i + dy][j - dx] == "S") \
                        or (grid[i - dy][j + dx] == "S" and grid[i + dy][j - dx] == "M")):
                    ans += 1
                    break

print(f"Answer to part 2: {ans}")
