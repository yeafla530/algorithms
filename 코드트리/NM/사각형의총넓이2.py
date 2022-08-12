n = int(input())
square = [[0 for _ in range(201)] for _ in range(201)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100


    for i in range(x1, x2):
        for j in range(y1, y2):
            square[i][j] = 1

sum = 0
for i in range(0, 201):
    for j in range(0, 201):
        if square[i][j] == 1:
            sum += 1

print(sum)