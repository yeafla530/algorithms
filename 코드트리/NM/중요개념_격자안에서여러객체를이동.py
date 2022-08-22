n = 4
count = [[0]*(n+1) for _ in range(n+1)]
next_count = [[0]*(n+1) for _ in range(n+1)]


# 충돌이 일어나는 구슬은 전부 지워준다
def remove_duplicate_marbles():
    # 충돌이 일어난 구슬들이 있는 위치만 빈 곳으로 설정하면 된다
    for i in range(1, n+1):
        for j in range(1, n+1):
            if count[i][j] >= 2:
                count[i][j] = 0

def get_next_pos(curr_x, curr_y):
    # 코딩의 간결함을 위해 
    # 문제 조건에 맞게 상하좌우 순서로
    # 방향을 정의합니다.
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    max_num, max_pos = a[curr_x][curr_y], (0, 0)
    
    # 각각의 방향에 대해 나아갈 수 있는 곳이 있는지 확인합니다.
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        
        # 범위안에 들어오는 격자 중 최댓값을 갱신합니다.
        if in_range(next_x, next_y) and a[next_x][next_y] > max_num:
            max_num = a[next_x][next_y]
            max_pos = (next_x, next_y)
            break
    
    return max_pos


def move(x, y):
    # 그 다음 위치 계산
    next_x, next_y = get_next_pos(x, y)
    # 그 다음 위치에 구슬의 개수를 1만큼 추가
    next_count[next_x][next_y] += 1




# Step 1
# 구슬을 전부 한번씩 움직임
def move_all():
    # Step 1-1
    # 그 다음 각 위치에서의 구슬 개수를 전부 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            next_count[i][j] = 0
    
    # Step 1-2
    # (i, j) 위치에 구슬이 있는 경우
    # 움직임을 시도해보고 그 결과를 전부 next_count에 기록
    for i in range(1, n+1):
        for j in range(1, n+1):
            if count[i][j] == 1:
                move(i, j)

    # Step 1-3
    # next_count 값을 count에 복사
    for i in range(1, n+1):
        for j in range(1, n+1):
            count[i][j] = next_count[i][j]


# 조건에 맞춰 시뮬레이션 진행
def simulate():
    # Step1
    # 구슬을 한번씩 움직여 본다
    move_all()

    # Step2
    # 움직임 이후에 충돌이 일어나는 구슬들을 골라 목록에서 지워준다
    remove_duplicate_marbles()

# t초간 시뮬레이션 진행
for _ in range(t):
    simulate()