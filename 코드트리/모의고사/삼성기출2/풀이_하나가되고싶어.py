import sys
from collections import deque

INT_MAX = sys.maxsize

# 변수 선언 및 입력:

n = int(input())
grid = [
    list(input())
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

blocks = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == '#'
]
bfs_q = deque()

ans = INT_MAX


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] != '#'


def bfs():
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()

        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                bfs_q.append((nx, ny))


def is_possible():
    # visited 값을 초기화합니다.
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # 빈공간으로 이루어진 그룹이 몇 개인지 판단합니다.
    group_cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.' and not visited[i][j]:
                group_cnt += 1

                visited[i][j] = True
                bfs_q.append((i, j))
                bfs()

    # 그룹이 정확히 1개인 경우에만 올바릅니다.
    return group_cnt == 1


def find_min_cnt(idx, cnt):
    global ans

    # 벽을 6개를 초과하여 제거하는 경우는 불가능합니다.
    if cnt > 6:
        return

    # 특정 조합에 대해
    if idx == len(blocks):
        # 전부 하나로 이어져 있다면 답을 갱신합니다.
        print(grid)
        if is_possible():
            ans = min(ans, cnt)

        return

    x, y = blocks[idx]

    grid[x][y] = '.'
    find_min_cnt(idx + 1, cnt + 1)
    grid[x][y] = '#'

    find_min_cnt(idx + 1, cnt)


find_min_cnt(0, 0)

if ans == INT_MAX:
    ans = -1

print(ans)