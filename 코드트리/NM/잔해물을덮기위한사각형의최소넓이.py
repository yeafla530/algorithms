point = [tuple(map(int, input().split())) for _ in range(2)]
area = [[0 for _ in range(2001)] for _ in range(2001)]

for idx, (x1, y1, x2, y2) in enumerate(point, start=1):
    x1, y1, x2, y2 = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000
    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = idx


min_x, min_y, max_x, max_y = 2001, 2001, 0, 0
first_rect_exist = False
for i in range(2001):
    for j in range(2001):
        if area[i][j] == 1:
            first_rect_exist = True
            min_x = min(min_x, i)
            min_y = min(min_y, j)
            max_x = max(max_x, i)
            max_y = max(max_y, j)
            
if not first_rect_exist:
    area = 0
# Case 2. 첫 번째 직사각형이 남아있다면, 넓이를 계산합니다.
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
print(area)