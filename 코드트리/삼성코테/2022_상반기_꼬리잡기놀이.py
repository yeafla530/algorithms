import sys
si = sys.stdin.readline
# 격자의 크기 n, 팀의 개수 m, 라운드 수 k
# k번의 라운드 동안 각 팀이 얻게되는 점수의 총합을 출력
n, m, k = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(n)]

## 어떤 자료에 저장할것인가
# 1. 팀을 어떻게 저장하나 
    # 1-1.이동도 시키고 - 이동선에 따라서 
    # 1-2.방향도 바꿔야함
    # 1-3.충돌여부 파악
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def detect_line(sx, sy): # (sx, sy)가 머리사람일 때, 팀원들의 좌표 리스트를 돌려주는 함수
    teamates = [(sx, sy)]
    x, y = sx, sy
    # 꼬리쪽으로 이동
    while a[x][y] != 3:
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny): continue
            # 4가 없는 선로가 있을 수 있다
            if len(teamates) >= 2 and (nx, ny) == teamates[-2]: continue # 머리 쪽으로 돌아가지 않고
            if a[x][y] == 1 and a[nx][ny] == 3: continue # 머리인 경우에는 꼬리로 가지 않고 
            if a[nx][ny] not in [2, 3]: continue # 이동선 위를 벗어나지 않는 방향

            x, y = nx, ny
            # print(x, y)
            break
        teamates.append((x, y))
    return teamates

def detect_whole_teams():
    heads = []
    # 1. 모든 팀을 찾고
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                heads.append((i, j))

    # 전체 팀 
    # 2. 각 팀을 한칸씩 이동시킬 예정
    teams = []
    for head in heads:
        teams.append(detect_line(*head))

    return teams

# 한 팀을 움직인다
def move_one_team(teamates):
    # 네방향 탐색해서 
    # 머리가 4가 있는 방향으로 이동
    x, y = teamates[0]
    # 머리가 이동할 좌표 찾기
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if not in_range(nx, ny): continue
        if a[nx][ny] not in [3, 4]: continue
        # 인접한 좌표 중 4가 써있는 위치 찾는다
        
        new_coords = []
        for teammate in teamates:
            cx, cy = teammate
            new_coords.append((nx, ny))
            nx, ny = cx, cy
            a[cx][cy] = 4

        for idx, (x, y) in enumerate(new_coords):
            if idx == 0: # 머리가 새롭게 이동한 위치
                a[x][y] = 1
            elif idx == len(new_coords) - 1: # 꼬리가 새롭게 이동한 위치
                a[x][y] = 3
            else: # 몸이 새롭게 이동한 위치
                a[x][y] = 2

        return

def move_whole_teams():
    # 각 팀을 찾는다
    # 머리만 모아둠
    teams = detect_whole_teams()
    
    # 한칸씩 이동시켜주는 함수
    for teamates in teams:
        move_one_team(teamates)
    

# 몇번째 라운드
def throw_ball(round_num) -> int:
    # 공을 조건에 맞게 던지고, 충돌하는 좌표 돌려주기
    round_num %= n * 4
    if round_num < n:
        # 던지기 시작위치
        x1, y1 = round_num, 0
        # 던지기 끝 위치
        x2, y2 = round_num, n
        dx, dy = 0, 1
    elif round_num < n * 2:
        x1, y1 = n-1, round_num - n
        x2, y2 = -1, round_num - n
        dx, dy = -1, 0

    elif round_num < n * 3:
        x1, y1 = (3 * n - 1) - round_num, n - 1
        x2, y2 = (3 * n - 1) - round_num, -1 
        dx, dy = 0, -1

    else:
        x1, y1 = 0, (4*n - 1) - round_num
        x2, y2 = n, (4*n - 1) - round_num
        dx, dy = 1, 0

    x, y = x1, y1
    # 충돌 확인 후 머리 꼬리를 뒤집고, 점수를 return
    # 끝 위치까지 한칸씩 이동
    while (x, y) != (x2, y2):
        # 머리 몸 꼬리
        if a[x][y] not in [0, 4]:
            return x, y
            # 1. 머리와 꼬리 반전
            # 2. 점수를 돌려줘야함
        x, y = x + dx, y + dy
    return None

def calculate(coord):
    # 모든팀을 찾는다
    teams = detect_whole_teams()
    for teammates in teams:
        # 팀을 하나씩 돌아준다
        for idx, teammate in enumerate(teammates, 1):
            # 공과 충돌한 팀의 팀원 찾음
            if teammate == coord:
                # print(teammate[0])
                x1, y1 = teammates[0]
                x2, y2 = teammates[-1]
                # 머리와 꼬리 반전
                a[x1][y1], a[x2][y2] = a[x2][y2], a[x1][y1]
                # 팀원의 index
                return idx * idx
    return 0

# 뼈대 구현
ans = 0 # 정답
for round_num in range(k):
    # 1. 각팀 이동시키기
    move_whole_teams()
    # print('------------------')
    # for i in range(n):
    #     for j in range(n):
    #         print(a[i][j], end=" ")
    #     print()
    # 2. 공던지기 
    coord = throw_ball(round_num)
    if coord is None:
        continue
    # 3. 팀 반전 및 점수계산
    ans += calculate(coord)

print(ans)