n = int(input())
point = [tuple(map(int, input().split())) for _ in range(n)]
area = [[0 for _ in range(201)] for _ in range(201)]

for x, y in point:
    x, y = x + 100, y + 100

    for i in range(x, x+8):
        for j in range(y, y+8):
            area[i][j] += 1


result = 0
for i in range(201):
    for j in range(201):
        if area[i][j] >= 1:
            result += 1

print(result)