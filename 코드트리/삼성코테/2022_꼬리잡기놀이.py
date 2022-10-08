# 격자의 크기 n, 팀의 개수 m, 라운드 수 k
# k번의 라운드 동안 각 팀이 얻게되는 점수의 총합을 출력
n, m, k = map(int, input().split())
board = [[0] * (n + 1)]
for i in range(n):
    board.append([0] + list(map(int, input().split())))

# 각 팀별 레일 위치 관리
v = [[] for _ in range(m + 1)]
# 각 팀별 tail 위치를 관리합니다.
tail = [0] * (m + 1)
visited = [[False] * (n + 1) for _ in range(n + 1)]
# 격자 내 레일에 각 팀 번호 적어줌
border_idx = [[0] * (n + 1) for _ in range(n + 1)]

ans = 0

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


# 초기 레일 만들기 위해 dfs이용
def dfs(x, y, idx):
    visited[x][y] = True
    # 레일체크
    border_idx[x][y] = idx
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if board[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue

        # 가장 처음 탐색할 때 2가 있는 방향으로 dfs진행
        if len(v[idx]) == 1 and board[nx][ny] != 2:
            continue

        v[idx].append((nx, ny))
        if board[nx][ny] == 3:
            tail[idx] = len(v[idx])
        dfs(nx, ny, idx)



# 초기 작업 진행
def init():
    cnt = 1
    # 레일을 벡터에 저장, 머리 사람을 우선 앞에 넣어줌
    # 팀 세기
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] == 1:
                v[cnt].append((i, j))
                cnt += 1

    # dfs를 통해 레일을 벡터 순서대로 넣어줌
    for i in range(1, m + 1):
        x, y = v[i][0]
        dfs(x, y, i)


def move_all():
    for i in range(1, m+1):
        # 각 팀에 대해 레일을 한칸씩 뒤로 이동시킴
        tmp = v[i][-1]
        for j in range(len(v[i])-1, 0, -1):
            v[i][j] = v[i][j-1]
        v[i][0] = tmp

init()
# 2. 각 라운드 마다 공을 던짐
# 3. 해당 선에 사람이 있는지 체크 후 최초 만나는 사람이 있으면 점수 획득 후 머리사람 꼬리사람 바꾸기
for i in range(i, k + 1):
    # 1. 머리사람 따라 한칸씩 이동
    move_all()