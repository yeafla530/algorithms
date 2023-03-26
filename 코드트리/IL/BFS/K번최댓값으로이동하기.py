# 내 풀이
# 1. 시작위치에서 출발해 인접한 숫자들 중 적혀있는 숫자가 x보다 작은 곳으로 전부 이동가능
# 2. 적혀있는 수들 중 최댓값으로 이동
# 3. 수가 여러개일 경우 행번호가 가장 작은곳으로 
# 4. 행번호도 같으면 열번호가 가장 작은곳으로 이동


# k번 반복한 후의 위치
# k번 반복하지 못해도 이동할 위치 없으면 멈춤
from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

check = [[0]*n for _ in range(n)]
num = grid[r][c]
q = deque()

dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    global num
    while len(q):
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and grid[nx][ny] < num and not check[nx][ny]:
                q.append((nx, ny))
                check[nx][ny] = 1


def find_next_pos(n):
    global num, r, c
    max_num = 0
    # print(check)
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if check[i][j] and max_num <= grid[i][j] and grid[i][j] != num:
                max_num = grid[i][j]
                # if n != k-1:
                r, c = i, j
    
    num = max_num
    # print(num)

def clear_check():
    for i in range(n):
        for j in range(n):
            check[i][j] = 0

for i in range(k):
    clear_check()
    q.append((r, c))
    # print(r, c)
    check[r][c] = 1
    bfs()
    find_next_pos(n)


print(r+1, c+1)






import collections

NOT_EXISTS = (-1, -1)

n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 현재 위치
r, c = tuple(map(int, input().split()))
curr_cell = (r - 1, c - 1)

bfs_q = collections.deque()
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y, target_num):
    return in_range(x, y) and not visited[x][y] and \
           grid[x][y] < target_num


# visited 배열을 초기화 해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

            
def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    curr_x, curr_y = curr_cell
    visited[curr_x][curr_y] = True
    bfs_q.append(curr_cell)
    
    target_num = grid[curr_x][curr_y]
    
    # BFS 탐색을 수행합니다.
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            
            if can_go(new_x, new_y, target_num):
                bfs_q.append((new_x, new_y))
                visited[new_x][new_y] = True
            

# best 위치를 새로운 위치로 바꿔줘야 하는지를 판단합니다.
def need_update(best_pos, new_pos):
    # 첫 도달 가능한 위치라면
    # update가 필요합니다.
    if best_pos == NOT_EXISTS:
        return True
    
    best_x, best_y = best_pos
    new_x, new_y = new_pos
    
    # 숫자, -행, -열 순으로 더 큰 곳이 골라져야 합니다.
    return (grid[new_x][new_y], -new_x, -new_y) > \
           (grid[best_x][best_y], -best_x, -best_y)


# 가장 우선순위가 높은 위치를 찾아
# 위치를 이동합니다.
def move():
    global curr_cell
    
    # BFS 탐색을 위한 초기화 작업을 수행합니다.
    initialize_visited()
    
    # Step1. BFS를 진행하여 갈 수 있는 모든 위치를 탐색합니다.
    bfs()
    
    # Step2. 
    # 도달 할 수 있는 위치들 중
    # 가장 우선순위가 높은 위치를 구합니다.
    best_pos = NOT_EXISTS
    for i in range(n):
        for j in range(n):
            # 도달이 불가능하거나 현재 위치는 건너뜁니다.
            if not visited[i][j] or (i, j) == curr_cell:
                continue
            
            new_pos = (i, j)
            if need_update(best_pos, new_pos):
                best_pos = new_pos

    # Step3. 위치를 이동합니다.
    
    # 만약 움직일 위치가 없다면 종료합니다.
    if best_pos == NOT_EXISTS:
        return False
    # 움직일 위치가 있다면 이동합니다.
    else:
        curr_cell = best_pos
        return True

# k번에 걸쳐 움직이는 것을 반복합니다.
for _ in range(k):
    is_moved = move()

    # 움직이지 못했다면 바로 종료합니다.
    if not is_moved:
        break

final_x, final_y = curr_cell
print(final_x + 1, final_y + 1)


# 내 풀이 
from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
visited = [[0]*n for _ in range(n)]
NOT_EXISTS = (-1, -1)
curr_cell = (r-1, c-1)

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

q = deque()

def initial_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, target_num):
    return in_range(x, y) and not visited[x][y] and graph[x][y] < target_num

def bfs():
    curr_x, curr_y = curr_cell
    visited[curr_x][curr_y] = True
    q.append(curr_cell)
    
    target_num = graph[curr_x][curr_y]
    
    # BFS 탐색을 수행합니다.
    while q:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            
            if can_go(new_x, new_y, target_num):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True


def need_update(best_pos, new_pos):
    if best_pos == NOT_EXISTS:
        return True

    best_x, best_y = best_pos
    new_x, new_y = new_pos

    return (graph[new_x][new_y], -new_x, -new_y) > (graph[best_x][best_y], -best_x, -best_y)    


def move():
    global curr_cell

    initial_visited()

    bfs()

    best_pos = NOT_EXISTS

    for i in range(n):
        for j in range(n):
            if not visited[i][j] or (i, j) == curr_cell:
                continue
            
            new_pos = (i, j)
            if need_update(best_pos, new_pos):
                best_pos = new_pos
            

    if best_pos == NOT_EXISTS:
        return False
    else:
        curr_cell = best_pos
        return True


for _ in range(k):
    is_moved = move()

    if not is_moved:
        break

final_x, final_y = curr_cell
print(final_x+1, final_y+1)