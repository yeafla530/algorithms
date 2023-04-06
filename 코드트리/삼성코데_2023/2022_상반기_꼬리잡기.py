import sys

si = sys.stdin.readline
n, m, k = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(n)]
dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]

# 뼈대 만들기

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def detect_line(pos): # (sx, sy)가 머리 사람일 때 팀원들의 좌표 리스트 돌려주는 함수
    teammates = [pos]
    x, y = pos

    # 꼬리를 만날때까지 진행
    while a[x][y] != 3:
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            # 다음으로 보고 있는 좌표가 나의 오기 전 좌표가 아닌 경우
            # 머리쪽이 아닌 꼬리쪽으로 나아가기
            # 격자를 벗어나지 않고 / 머리쪽으로 다시 돌아가지 않으며 / 이동선 위를 벗어나지 않는다면
            if not in_range(nx, ny): continue
            if len(teammates) >= 2 and (nx, ny) == teammates[-2]: continue
            # 4가 없는 경로에서 머리에서 꼬리로 이동하면 안됨
            if a[x][y] == 1 and a[nx][ny] == 3: continue
            if a[nx][ny] not in [2, 3]: continue
            
            x, y = nx, ny
            break
        
        teammates.append((x, y))
    return teammates

# 모든 팀을 찾아서 돌려줌
def detect_whole_teams():
    # 1. 모든 머리를 찾고
    heads = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                heads.append((i, j))


    # 2. 각 팀을 찾는 함수
    teams = []
    for head in heads:
        teams.append(detect_line(head))

    return teams

def move_one_step(teammates): # teammates가 한 팀을 순서대로 쓴 경우
    # 머리가 이동할 좌표 찾기
    x, y = teammates[0]
    
    # 네 방향을 보면서
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        # 인접한 위치 중 4 찾기
        if not in_range(nx, ny): continue
        if a[nx][ny] not in [3, 4]: continue
        # 모든 머리 꼬리 이동시키기
        # 인접한 좌표 중 3, 4로 이동 (4가 없는 칸 존재)
        new_coords = []
        for teammate in teammates:
            cx, cy = teammate
            # 각 좌표가 어디로 갈지 적어줌 
            new_coords.append((nx, ny))
            nx, ny = cx, cy
            a[cx][cy] = 4

        for idx, (x, y) in enumerate(new_coords):
            if idx == 0: # 머리가 새롭게 이동한 위치
                a[x][y] = 1
            elif idx == len(new_coords) - 1: # 꼬리가 새롭게 이동한 위치
                a[x][y] = 3
            else: # 머리가 새롭게 이동한 위치
                a[x][y] = 2

        return


def move_whole_team():
    # 1. 모든 팀을 찾고
    teams = detect_whole_teams()

    # 2. 각 팀을 한칸씩 이동
    for teammates in teams:
        move_one_step(teammates)


def throw_ball(round_num) -> int:
    # 공을 조건에 맞게 던지고, 충돌하는 좌표 돌려주기
    round_num %= n * 4

    if round_num < n:
        x1, y1 = round_num, 0
        x2, y2 = round_num, n

    elif round_num < n * 2:
        x1, y1 = n-1, round_num - n
        x2, y2 = -1, round_num - n
    elif round_num < n * 3:
        x1, y1 = 3 * n - round_num - 1, n-1
        x2, y2 = 3 * n - round_num - 1,  -1
    else:
        x1, y1 = 0, 4 * n - round_num - 1
        x2, y2 = n, 4 * n - round_num - 1
    
    # 방향 설정
    dx, dy = (x2 - x1) // n , (y2 - y1) // n

    x, y = x1, y1
    # 끝까지 이동
    while (x, y) != (x2, y2):
        # 머리~꼬리
        if a[x][y] not in [0, 4]:
            return x, y            
        x, y = x + dx, y + dy
    
    return None

def calculate(coord):
    teams = detect_whole_teams()
    for teammates in teams:
        for idx, teammate in enumerate(teammates, 1):
            if teammate == (coord):
                x1, y1 = teammates[0]
                x2, y2 = teammates[-1]

                a[x1][y1], a[x2][y2] = a[x2][y2], a[x1][y1]
                return idx * idx
    return 0


ans = 0 # 정답

for round_num in range(k):
    # 1. 각 팀 머리 사람 이동
    move_whole_team()

    # 2. 공던지기 => 맞춘 위치 돌려주기
    coord = throw_ball(round_num) 
    
    if coord is None:
        continue
    # 3. 점수 계산 후 머리사람 변경
    ans += calculate(coord)



print(ans)