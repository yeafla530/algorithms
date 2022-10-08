# 격자의 크기 n, 박멸이 진행되는 년 수 m, 제초제의 확산 범위 k, 제초제가 남아있는 년 수 c
n, m, k, c = map(int, input().split())
tree = [[0] * (n + 1)]
for _ in range(n):
    tree.append([0] + list(map(int, input().split())))

add_tree = [[0] * (n + 1) for _ in range(n + 1)]

herb = [[0] * (n + 1) for _ in range(n + 1)]
ans = 0

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]


def is_out_range(x, y):
    return not (1 <= x < n + 1 and 1 <= y < n + 1)


def step_one():
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            # 벽이 있으면 세지 않는다
            if tree[x][y] <= 0:
                continue
            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                # 범위 안에 있는지 체크, 나무가 있으면
                if is_out_range(nx, ny):
                    continue
                if tree[nx][ny] > 0:
                    # 성장
                    # tree[x][y] += 1
                    cnt += 1

            tree[x][y] += cnt


# 기존에 있었던 나무들은 아무것도 없는 칸에 번식 진행
def step_two():
    # 동시에 진행됨 # 새로운 배열 사용
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            add_tree[i][j] = 0

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if tree[x][y] > 0:
                # 빈 자리 count
                cnt = 0
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy

                    # 범위를 벗어남
                    if is_out_range(nx, ny):
                        continue
                    # 벽 / 다른나무 / 제초제 모두 없어야함
                    # 제초제 있으면
                    if herb[nx][ny]:
                        continue
                    # 나무가 비어있으면
                    if tree[nx][ny] == 0:
                        cnt += 1

                # 비어있는 칸에 확산
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if is_out_range(nx, ny):
                        continue
                    if herb[nx][ny]:
                        continue
                    if tree[nx][ny] == 0:
                        add_tree[nx][ny] += tree[x][y] // cnt
    # add_tree에 있는 값 옮기기
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tree[i][j] += add_tree[i][j]


# 제초제 기간을 1년 감소 시킨다
def delete_herb():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if herb[i][j] > 0:
                herb[i][j] -= 1


# 가장 많이 박멸되는 칸에 제초제를 뿌린다
nxs = [1, -1, 1, -1]
nys = [1, 1, -1, -1]


def step_three():
    global ans
    # 돈다
    # 최고 많이 박멸되는 수, 그 나무의 index
    max_result, max_x, max_y = 0, 1, 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 나무가 없으면 안됨
            if tree[i][j] <= 0:
                continue

            # 배열 돌때마다 박멸 개수 세기
            cnt = tree[i][j]
            for dx, dy in zip(nxs, nys):
                nx = i
                ny = j
                # k범위만큼 뻗어나감
                for _ in range(k):
                    nx = nx + dx
                    ny = ny + dy
                    # 범위 벗어나면 안됨
                    if is_out_range(nx, ny):
                        break
                    # 벽 / 나무가 없는 곳
                    if tree[nx][ny] <= 0:
                        break
                    cnt += tree[nx][ny]

            if max_result < cnt:
                max_result = cnt
                max_x = i
                max_y = j

    # 개수 추가
    ans += max_result

    # 찾은 칸에 제초제 뿌리기
    if tree[max_x][max_y] > 0:
        tree[max_x][max_y] = 0
        herb[max_x][max_y] = c

        for dx, dy in zip(nxs, nys):
            nx = max_x
            ny = max_y

            for _ in range(k):
                nx += dx
                ny += dy

                if is_out_range(nx, ny):
                    break
                # 벽인 경우
                if tree[nx][ny] < 0:
                    break
                if tree[nx][ny] == 0:
                    herb[nx][ny] = c
                    break

                tree[nx][ny] = 0
                herb[nx][ny] = c


for _ in range(m):
    # 1단계 : 인접한 네 개의 칸 중 나무가 있는 칸 수만큼 나무가 성장
    step_one()
    print(tree)
    # 2단계 : 기존에 있었던 나무들은 아무것도 없는 칸에 번식 진행
    step_two()
    print(tree)
    # # 제초제 기간을 1년 감소 시킨다
    delete_herb()
    print(tree)
    # # 3단계 : 가장 많이 박멸되는 칸에 제초제를 뿌린다
    step_three()
    print(tree)
    print(ans)

print(ans)