from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


group = [[0]*n for _ in range(n)]
q = deque()
visited = [[0]*n for _ in range(n)]
group_count = [0]
ans = 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
def bfs():
    # 상좌하우
    dxs = [-1, 0, 1, 0]
    dys = [0, -1, 0, 1]
    count = 0
    while q:
        x, y = q.popleft()

        group[x][y] = cnt
        count += 1
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny] and board[x][y] == board[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))


    group_count.append(count)
# 각자 다른 그룹 구하기
cnt = 0
def initialize():
    global cnt
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
    #  bfs사용해서 서로다른 그룹 구하기
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += 1
                q.append((i, j))
                visited[i][j] = 1
                bfs()

# 예술성 점수 구하기
def count_score():
    global ans
    # 하 좌
    dxs = [1, 0]
    dys = [0, 1]
    # 점수 구하기
    for x in range(n):
        for y in range(n):
            for dx, dy in  zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and group[x][y] != group[nx][ny]:
                    a = group[x][y]
                    b = group[nx][ny]
                    ans += (group_count[a] + group_count[b]) * board[x][y] * board[nx][ny]
                    # print(ans)


    # (a 칸 수 + b에 칸 수 ) x a 숫자 값 x b를 숫자 값 x 서로 맞닿아 있는 변의 수
    # 닿는 면 개수 구하기

# 시계방향 회전
def next_rotate(i1, j1, i2, j2, cnt):
    len = i2-i1
    # print(len)
    # 5*5, 2*2
    temp = [[0] * n for _ in range(n)]
    # print("++++++++++++++++++++ start")

    for i in range(i1, i2):
        for j in range(j1, j2):
            temp[i][j] = board[i][j]


    for _ in range(cnt):
        temp = list(map(list, zip(*temp[::-1])))

    # print(temp)
    x = i1
    y = j1
    for i in range(n):
        for j in range(n):
            if temp[i][j]:
                # print(x, y)
                copy_board[x][y] = temp[i][j]
                y += 1
                if y == j2:
                    y = j1
                    x += 1

    # print(copy_board)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$ end")


copy_board = [[0]*n for _ in range(n)]
def rotate_initial():
    for i in range(n):
        for j in range(n):
            copy_board[i][j] = board[i][j]

def rotate():
    rotate_initial()
    # 전체를 돌려준다
    next_rotate(0, 0, n, n, 3)

    m = n // 2
    # 4군데를 시계 반대방향 3번 돌려준다
    next_rotate(0, 0, m, m, 1)
    next_rotate(0, m+1, m, n, 1)
    next_rotate(m+1, 0, n, m, 1)
    next_rotate(m+1, m+1, n, n, 1)

    for i in range(n):
        for j in range(n):
            board[i][j] = copy_board[i][j]

    # print(board)

# print(group_count)
# 4번 회전
for _ in range(4):
    initialize()
    # 1. 예술성 점수 구하기
    count_score()
    # print("============================")
    # 2. 회전하기
    rotate()
    # print(board)


print(ans)