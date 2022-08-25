import sys

COIN_NUM = 9
INT_MAX = sys.maxsize

# n개중 m개 뽑기
n = int(input())
m = 3

# 입력받은 값
grid = [input() for _ in range(n)]
# coin 위치
coin_pos = list()
# 선택된 위치
selected_pos = list()

start_pos = (-1, -1)
end_pos = (-1, -1)

# 최솟값 구하기
ans = INT_MAX

# 출발점, 도착점 구하기
for i in range(n):
    for j in range(n):
        if grid[i][j] == "S":
            start_pos = (i,j)
        elif grid[i][j] == "E":
            end_pos = (i, j)


# 동전 오름차순으로 위치 넣기
for num in range(1, COIN_NUM+1):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == str(num):
                coin_pos.append((i, j))


# 움직인 횟수  구하기
def dist(a, b):
    (ax, ay), (bx, by) = a, b
    return abs(ax - bx) + abs(ay - by)

# 이동경로 구하기
def calc():
    nun_moves = dist(start_pos, selected_pos[0])
    for i in range(m-1):
        nun_moves += dist(selected_pos[i], selected_pos[i+1])
    nun_moves += dist(selected_pos[m-1], end_pos)

    return nun_moves


def find_min_moves(curr_idx, cnt):
    global ans
    # 종료조건
    if cnt == m:
        ans = min(ans, calc())
        return

    if curr_idx == len(coin_pos):
        return

    # curr_idx에 있는 동전을 선택하지 않은 경우
    find_min_moves(curr_idx+1, cnt)
    # 선택한 경우
    selected_pos.append(coin_pos[curr_idx])
    find_min_moves(curr_idx+1, cnt+1)
    selected_pos.pop()
    
# 최소로 움직인 횟수구하기
find_min_moves(0, 0)

if ans == INT_MAX:
    ans = -1

print(ans)