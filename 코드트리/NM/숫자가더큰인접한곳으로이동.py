# 나의 풀이
n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

start = r-1
end = c-1

def in_range(s, e):
    return 0 <= s < n and 0 <= e < n



# 상하좌우숫자가 현재 수보다 전부 낮을때
cur_num = arr[start][end]
print(cur_num, end=" ")
while True:
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx = start + dx
        ny = end + dy
        if in_range(nx, ny) and arr[nx][ny] > cur_num:
            start = nx
            end = ny
            cur_num = arr[nx][ny]
            print(cur_num, end=" ")
            break
        cnt += 1
    
    if cnt == 4:
        break


## 정리된 코드 - 해답 코드
# simulate 정의 중요
n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

start = r-1
end = c-1
# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 방문하게 되는 숫자들을 담을 곳입니다.
visited_nums = []

def in_range(s, e):
    return 0 <= s < n and 0 <= e < n

# 1초동안 일어나는 일
def simulate():
    global start, end
    for dx, dy in zip(dxs, dys):
        nx = start + dx
        ny = end + dy
        if in_range(nx, ny) and arr[nx][ny] > arr[start][end]:
            start = nx
            end = ny
            return True
    return False
# 상하좌우숫자가 현재 수보다 전부 낮을때
visited_nums.append(arr[start][end])
while True:
    # 조건에 맞춰 움직여봅니다.
    greater_number_exist = simulate()
    
    if not greater_number_exist:
        break
    visited_nums.append(arr[start][end])

print(*visited_nums)