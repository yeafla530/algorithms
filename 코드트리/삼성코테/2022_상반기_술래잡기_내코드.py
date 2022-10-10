# 격자 크기 n, m명의 도망자, h개 나무, k번 턴 반복
n, m, h, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
next_graph = [[[] for _ in range(n)] for _ in range(n)]
tree = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
# 술래 x, y
cur_x, cur_y = n // 2, n // 2
dir_num = 0
ans = 0

# 위 오 아 왼
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
# 도망자의 위치 (x, y)와 이동 방법 d
# d가 1인 경우 좌우로 움직임을, 2인 경우 상하로만 움직임
for _ in range(m):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1

    # 상: 0, 오: 1, 하: 2, 좌: 3
    graph[x][y].append(d)

print()


for _ in range(h):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    tree[x][y] = 1

# print(tree)


# 격자 벗어나는지
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

print('초기')
for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()
print("++++++++++++++++++++++++++++++")
# 술래 위치는 n//2부터

# 도망자 움직이기
def move_hidden():
    # 맨 처음에 오른쪽, 아래쪽 시작
    for i in range(n):
        for j in range(n):
            next_graph[i][j] = []
    for x in range(n):
        for y in range(n):
            if len(graph[x][y]):
                if abs(cur_x - x) + abs(cur_y - y) > 3:
                    continue
                for _ in range(len(graph[x][y])):
                    d = graph[x][y].pop()
                    # 술래와 거리가 3이하인 도망자만 움직임
                    nx = x + dxs[d]
                    ny = y + dys[d]

                    ## 바라보는 방향 움직 => 격자 안벗어남
                    if in_range(nx, ny):
                        ### 움직이는 칸에 술래 있으면 움직이지 않음
                        if nx == cur_x and ny == cur_y:
                            next_graph[x][y].append(d)
                            continue
                        ### 움직이는 칸에 술래 없으면 이동 (나무있어도 괜찮음)
                        next_graph[nx][ny].append(d)



                    ## 격자 벗어남
                    else:
                        ### 반대 방향으로 바라봄
                        d ^= 2

                        ### 바라보는 방향으로 1칸 이동시 술래 없으면 이동, 있으면 이동 x
                        nx = x + dxs[d]
                        ny = y + dys[d]

                        if nx == cur_x and ny == cur_y:
                            next_graph[x][y].append(d)
                            continue
                        next_graph[nx][ny].append(d)



    for i in range(n):
        for j in range(n):
            graph[i][j] = next_graph[i][j]

    for i in range(n):
        for j in range(n):
            print(next_graph[i][j], end=" ")
        print()
    print("++++++++++++++++++++++++++++++")


def clear():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

    visited[0][0] = 1


move_num = 1
count = 1


# 안 => 밖
def move1():
    global cur_x, cur_y, dir_num, count, move_num
    nx = cur_x + dxs[dir_num]
    ny = cur_y + dys[dir_num]
    if nx == n // 2 and ny == n // 2:
        move_num = 1
        count = 1

    if in_range(nx, ny):
        cur_x = nx
        cur_y = ny

    else:
        cur_x = 0
        cur_y = 0
        move_num -= 1
        count = move_num
        dir_num = 2

        clear()
    # print("c", count)
    if count == 0:
        dir_num = (dir_num + 1) % 4
        if dir_num == 0 or dir_num == 2:
            move_num += 1
        count = move_num
        # print("dir_num, count", dir_num, count)




# 밖 => 안
def move2():
    global dir_num, cur_x, cur_y

    visited[cur_x][cur_y] = 1
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    nx = cur_x + dxs[dir_num]
    ny = cur_y + dys[dir_num]

    if not in_range(nx, ny) or visited[nx][ny]:
        dir_num = (dir_num + 1) % 4

    cur_x = cur_x + dxs[dir_num]
    cur_y = cur_y + dys[dir_num]





# 술래 움직이기
def move_seeker(turn):
    global count
    count -= 1
    # 달팽이 모양으로 반복하여 이동함 => 끝까지 이동하면 반대 방향으로 진행
    # 안 => 밖
    turn = turn % (2 * n * n - 1)
    if turn <= n * n - 1:
        move1()
    # 밖 => 안
    else:
        move2()

    print("cur_x, cur_y", cur_x, cur_y)


# 점수 계산하기
def calc_score():
    # 술래가 그 다음 방향을 바라봄
    # 해당 방향에 도망자가 있으면 잡는다 (3칸까지)
    count = 0
    for i in range(3):
        nx = cur_x + (dxs[dir_num] * i)
        ny = cur_y + (dys[dir_num] * i)
        # print(nx, ny, graph[nx][ny])
        if not in_range(nx, ny):
            continue
        ## 나무에 가려진 도망자는 잡지 못함
        if len(graph[nx][ny]):
            if tree[nx][ny]:
                continue
            count += len(graph[nx][ny])
            graph[nx][ny] = []
        # print(nx, ny, graph[nx][ny])

    ## 턴 횟수 x 도망자 수
    return count


for t in range(1, k+1):
    # 1. 도망자가 움직임
    move_hidden()

    # 2. 술래가 움직임
    move_seeker(t)
    # print(cur_x, cur_y, dir_num)
    # 3. 점수내기
    ans += t * calc_score()
    # print(ans)


print(ans)
