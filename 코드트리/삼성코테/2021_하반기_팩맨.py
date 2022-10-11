n = 4
m, t = map(int, input().split())
r, c = map(lambda x: int(x) -1, input().split())
graph = [[[] for _ in range (n)] for _ in range(n)]
next_grahp = [[[] for _ in range (n)] for _ in range(n)]
packman_graph = [[0]*n for _ in range(n)]
dead_graph = [[[] for _ in range(n)] for _ in range(n)]
egg_graph = [[[] for _ in range(n)] for _ in range(n)]
result = 0

packman_graph[r][c] = 1
for _ in range(m):
    x, y, d = map(lambda x: int(x) - 1, input().split())
    graph[x][y].append((2, d))


# 1. 몬스터 복제 시도
def try_monster_copy():
    # 알을 몬스터와 같은 위치에 복제한다
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]):
                for num, d in graph[i][j]:
                    egg_graph.append(d)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def in_dead(x, y):
    if len(dead_graph[x][y]):
        return True
    return False

def in_packman(x, y):
    if packman_graph[x][y]:
        return True
    return False

visit_dir = [0] * 8
# 2, 몬스터 움직이기
def move_monster():
    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, -1, -1, -1, 0, 1, 1, 1]

    # next graph필요
    for i in range(n):
        for j in range(n):
            next_grahp[i][j] = []
    # 자신이 가진 방향으로 이동
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]):
                for num, d in graph[i][j]:
                    for x in range(8):
                        visit_dir[x] = 0

                    is_move = False
                    while True:
                        # 이미 방문했던 위치나 움직인 경우
                        if is_move or visit_dir[d]:
                            break
                        # 가고 싶은 자리
                        nx = i + dxs[d]
                        ny = j + dys[d]
                        visit_dir[d] = 1
                        # 움직이는 방향에
                        # 몬스터 시체 or 팩맨 or 격자 벗어남 => 반시계 45도 회전
                        if not in_range(nx, ny):
                            d = (d + 1) % 8
                            continue
                        if in_dead(nx, ny):
                            d = (d + 1) % 8
                            continue
                        if in_packman(nx, ny):
                            d = (d + 1) % 8
                            continue

                        is_move = True
                        # 해당 방향으로 갈 수 없다면 될때까지 반복
                        # 모두 움직일 수 없으면 움직이지 않기

def calc_score(x, y, dir_arr):
    dxs = [-1, 0, 1, 0]
    dys = [0, -1, 0, 1]
    nx = x
    ny = y
    value = 0

    for di in dir_arr:
        nx = nx + dxs[di]
        ny = ny + dys[di]
        if not in_range(nx, ny):
            return 0
        if len(graph[nx][ny]):
            value += len(graph[nx][ny])

    print(value)
    return value



# 팩맨 이동 담기
dir_arr = []
result_dir_arr = []
max_score = 0
# 3. 팩맨이동
def move_packman():
    # 상하좌우로만 움직일 수 있음 (3칸)

    # 팩맨 위치 찾기
    for i in range(n):
        for j in range(n):
            if packman_graph[i][j]:
                x = i
                y = j

    # 몬스터 가장 많이 먹을 수 있는 방향으로 이동
    # 상 좌 하 우 우선순위
    # 테스트용
    dir_arr = []
    result_dir_arr = []
    # 최대 경로 담아줌

    def choose(cnt):
        global max_score, result_dir_arr
        if cnt == 3:
            print(dir_arr)
            score = calc_score(x, y, dir_arr)
            # 해당 경로가 최대 경로면
            # 원래 위치에서 이동
            if max_score < score:
                max_score = score
                result_dir_arr = dir_arr

            return

        for i in range(4):
            dir_arr.append(i)
            choose(cnt+1)
            dir_arr.pop()

    choose(0)

    print(result_dir_arr)
    # 알은 먹지 않는다, 움직이기 전 함께 있던 몬스터도 먹지 않는다
    # 몬스터를 먹는다 => 시체 남김

# 4. 시체 소멸
# def delete_dead():
    # 2턴 후에 사라진다


# 5. 복제 완성
# def complete_copy():
    # 알 형태 몬스터 태어남


# 팩맨 : 1, 몬스터: 2, 알: 3, 시체: 4
for _ in range(t):
    # 1. 몬스터 복제 시도
    try_monster_copy()
    # 2. 몬스터 이동
    move_monster()
    # # 3. 팩맨 이동
    move_packman()
    # # 4. 시체 소멸
    # delete_dead()
    # # 5. 복제완성
    # complete_copy()