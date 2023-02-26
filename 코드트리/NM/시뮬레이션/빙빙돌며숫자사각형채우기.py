# 별도의 2차원 배열 활용
# 오른쪽 아래 왼쪽 위쪽 순서로 계속 이동 => 0, 1, 2, 3 반복
# 방향 트는 조건은 현재 방향으로 더 갔을 때 격자 벗어나게 되거나 
# 이미 방문했던 적이 있어 숫자가 이미 적힌 경우

# 체크 조건
# 1. 격자 벗어나는지
# 2. 이미 방문했던 곳 아닌지

# 방향
# 0, 1, 2에서는 1씩 늘어나며
# 3의 경우 0이 되므로 다음방향은 (dir + 1) % 4로 구할 수 있다

n, m = map(int, input().split())
answer = [[0]*m for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 오 아 왼 위
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0 # 시작은 (0, 0)
dir_num = 0 # 방향 전환

answer[x][y] = 1

# 2부터 시작 n*n까지 표시 
for i in range(2, n*m+1):
    nx = x + dxs[dir_num]
    ny = y + dys[dir_num]

    # 더이상 나아갈 수 없다면 시계방향으로 90도 회전
    # 1. 격자를 벗어나거나 이미 갔던 곳일경우 방향 전환 
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x = x + dxs[dir_num]
    y = y + dys[dir_num]

    answer[x][y] = i

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=" ")
    print()


