OFFSSET = 100
AREA = 201

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
area = [[0 for _ in range(AREA+1)] for _ in range(AREA+1)]
# print(arr)

for idx, (x1, y1, x2, y2) in enumerate(arr, start = 1):
    x1 += OFFSSET
    y1 += OFFSSET
    x2 += OFFSSET
    y2 += OFFSSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            if idx % 2:
                # 빨간색
                area[i][j] = 1
            else:
                area[i][j] = 2

count = 0
for i in range(AREA+1):
    for j in range(AREA+1):
        if area[i][j] == 2:
            count += 1

print(count)