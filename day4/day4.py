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

print(ans)
