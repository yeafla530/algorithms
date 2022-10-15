from collections import deque

n, q = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(2 ** n)]
levels = list(map(int, input().split()))
w = 2 ** n

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

max_cnt = 0


def bfs():
    count = 0
    while que:
        x, y = que.popleft()
        count += 1
        # print(count, x, y)
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and ices[nx][ny] != 0 and not visited[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = 1

    return count


# 2. 레벨 범위만큼 회전시킨다
def spin(x, y, verse, level):
    arr = [[0] * verse for _ in range(verse)]
    new_j = 0
    for i in range(verse):
        for j in range(verse):
            arr[i][j] = ices[i + x][j + y]

    new_arr = [[0] * verse for _ in range(verse)]
    if level == 0:
        for i in range(verse):
            for j in range(verse):
                new_arr[i][j] = arr[i][j]

    elif level >= 1:
        next_verse = 2 ** (level - 1)

        for i in range(0, verse, next_verse):
            for j in range(0, verse, next_verse):

                for a in range(i, i + next_verse):
                    for b in range(j, j + next_verse):
                        if i == 0 and j == 0:
                            new_arr[a][b] = arr[a + next_verse][b]
                        elif i == 0 and j == next_verse:
                            new_arr[a][b] = arr[a][b - next_verse]
                        elif i == next_verse and j == 0:
                            new_arr[a][b] = arr[a][b + next_verse]
                        elif i == next_verse and j == next_verse:
                            new_arr[a][b] = arr[a - next_verse][b]

    for i in range(verse):
        for j in range(verse):
            ices[i + x][j + y] = new_arr[i][j]


def in_range(x, y):
    return 0 <= x < 2 ** n and 0 <= y < 2 ** n


new_ices = [[0] * (2 ** n) for _ in range(2 ** n)]
# 좌측 상단에 있는 빙하를 특정 범위를 선택해서 회전시키게 되면
# 다른 상하좌우의 인접한 격자들도 똑같은 크기만큼 회전하게 됩니다
for i in range(q):
    level = levels[i]
    verse = 2 ** level
    for i in range(2 ** n):
        for j in range(2 ** n):
            new_ices[i][j] = 0
    # 1. 범위를 선택한다
    for i in range(0, w, verse):
        for j in range(0, w, verse):
            # 2. 레벨 범위만큼 회전시킨다
            spin(i, j, verse, level)

    # 3. 빙하가 녹는다 (인접한 얼음)
    for x in range(2 ** n):
        for y in range(2 ** n):
            if ices[x][y] == 0:
                continue

            count = 0
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy

                if in_range(nx, ny) and ices[nx][ny] != 0:
                    count += 1

            # print(count)

            if count < 3:
                new_ices[x][y] = ices[x][y] - 1
            else:
                new_ices[x][y] = ices[x][y]

    # print(new_ices)
    for i in range(2 ** n):
        for j in range(2 ** n):
            ices[i][j] = new_ices[i][j]

    # print(ices)

total_ices = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        total_ices += ices[i][j]
que = deque()

visited = [[0] * (2 ** n) for _ in range(2 ** n)]

cnt = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if ices[i][j] and not visited[i][j]:
            visited[i][j] = 1
            que.append((i, j))
            cnt = bfs()

            max_cnt = max(max_cnt, cnt)

print(total_ices)
print(max_cnt)