# 격자의 크기 n, 박멸이 진행되는 년 수 m, 제초제의 확산 범위 k, 제초제가 남아있는 년 수 c
n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
copy_tree = [[0] * n for _ in range(n)]
drug = [[0] * n for _ in range(n)]

result = 0

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

nxs = [1, -1, 1, -1]
nys = [-1, -1, 1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def count_tree():
    global graph
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0 and not drug[x][y]:
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if in_range(nx, ny) and graph[nx][ny] > 0 and not_drug(nx, ny):
                        graph[x][y] += 1


def not_drug(nx, ny):
    if drug[nx][ny]:
        return False

    return True


def grow_tree():
    for x in range(n):
        for y in range(n):
            arr = []
            count = 0
            tree_count = graph[x][y]

            if graph[x][y] <= 0 or drug[x][y]:
                continue

            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy

                if in_range(nx, ny) and not_drug(nx, ny) and graph[nx][ny] == 0:
                    arr.append((nx, ny))
                    count += 1
            # print(arr)
            if count:
                tree_count = graph[x][y] // count
                for dx, dy in arr:
                    copy_tree[dx][dy] += tree_count

    for i in range(n):
        for j in range(n):
            graph[i][j] += copy_tree[i][j]
            copy_tree[i][j] = 0


def can_go(x, y):
    if in_range(x, y) and not_drug(x, y):
        return True

    return False


def mina_drug():
    global drug
    for i in range(n):
        for j in range(n):
            if drug[i][j]:
                if drug[i][j] == 1:
                    graph[i][j] = 0
                drug[i][j] -= 1


def pos_drug():
    max_result = 0
    rx = 0
    ry = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0 and not_drug(x, y):
                # print(graph[x][y])
                del_tree = graph[x][y]
                for dx, dy in zip(nxs, nys):
                    for t in range(1, k + 1):
                        nx = x + (dx * t)
                        ny = y + (dy * t)
                        if not can_go(nx, ny):
                            break
                        if graph[nx][ny] <= 0:
                            break
                        del_tree += graph[nx][ny]

                if del_tree > max_result:
                    rx = x
                    ry = y
                    max_result = del_tree

    mina_drug()

    # 제초제를 뿌림
    graph[rx][ry] = 0
    drug[rx][ry] = c
    # print(rx, ry)
    for dx, dy in zip(nxs, nys):
        for t in range(1, k + 1):
            nx = rx + (dx * t)
            ny = ry + (dy * t)
            if not can_go(nx, ny):
                break
            if graph[nx][ny] <= 0:
                break
            # if graph[nx][ny] == 1:
            # drug[nx][ny] = c

            graph[nx][ny] = 0
            drug[nx][ny] = c
    print(max_result)
    print(drug)

    return max_result


# 1. 시작
for i in range(m):
    # 2. 성장
    count_tree()
    print('count', graph)
    # 3. 번식
    grow_tree()
    print('grow',graph)

    # 4. 제초제 뿌릴 위치 선정
    result += pos_drug()
    print('pos', graph)

print(result)