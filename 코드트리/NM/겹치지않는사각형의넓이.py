area = [[0 for _ in range(2001)] for _ in range(2001)]
point = [tuple(map(int, input().split())) for _ in range(3)]

for idx, (x1, y1, x2, y2) in enumerate(point, start=1):
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = idx

sum = 0
for i in range(2001):
    for j in range(2001):
        if area[i][j] == 1 or area[i][j] == 2:
            sum += 1

print(sum)