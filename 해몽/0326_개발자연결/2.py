import sys
si = sys.stdin.readline

available = [list(map(int, si().split())) for _ in range(4)] # 각 격자의 사용 가능 여부
visit = [[False, False, False] for _ in range(4)] # 각 격자의 사용 여부


ans = 0 # 정답 변수

# 마지막으로 도착한 격자의 좌표 (x, y)이고 
# 이때까지 사용한 격자의 개수가 len인 상황에서, 
# 모든 이후 상황을 탐색해주는 완전탐색 함수
def backtracking(x, y, len): 
    global ans
    if len >= 2: # 사용한 격자의 개수가 2개 이상이라면 정답 증가
        ans += 1

    visit[x][y] = True # 중복된 방문 막기위한 방문 처리

    dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (-1, 0), (0, 1), (1, 0)]
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        # (x, y) => (nx, ny)로 이동하고 싶은 상황
        if not (0 <= nx < 4 and 0 <= ny < 3) : continue # 범위 
        if available[nx][ny] == 0: continue             # 고장나면 안됨
        if visit[nx][ny]: continue                      # 이미 사용한 격자면 안됨

        backtracking(nx, ny, len+1)

    visit[x][y] = False # 이후에 다시 이 격자를 활성화 시켜주기 위해 방문 처리 회수


for i in range(4):
    for j in range(3):
        if available[i][j] == 1:
            backtracking(i, j, 1)


print(ans)


'''
1 1 1
1 1 1
1 1 1
1 1 1
=> 193912

0 1 0
1 1 1
1 0 0
0 0 1
=> 96
'''