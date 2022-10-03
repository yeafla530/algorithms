# 1. 완전탐색 : 빈 장소 찾기 
# 2. 그래프 탐색 : 최대 마을의 크기 최대값 찾기, DFS, BFS로 풀수있다
# 마을 구분하기 문제랑 똑같음
# n^4 까지 해서 만점을 받을 수있는 문제였다

# 그래프 탐색 문제 풀어보기!!

##### + 최적화
# O(n^4) => O(n^2)으로 줄일 수 있는 법
# n = 5000일때 
# 새로운 사람 집어넣지 않고, DFS, BFS를 먼저 돌려줌
# 1번마을 2명 , 2번마을 3명, 3번마을 10명 먼저 전처리해줌
# 새로운 사람이 어디 들어왔을 때 그 사람이 포함된 마을의 수는 상하좌우로 인접한 마을의 사람수
# 상하좌우 인접한 곳의 마을이 겹치면 어떡함 ? => 중복될수있음
# 겹치지 않도록 한번씩만 더해준다
# 인접한 4개의 마을을 보면서 누적합 해주는 함수


## 꼭 새로운 사람이 들어가 있는 마을만 최대인가? 라는 생각을 할 수 있다
# 마을을 자를 때 주변에 0이 있기 때문에 잘린거기 때문에
# 대왕마을도 언젠가 새로 들어온 사람과 만날 수 있다
# 벽이 있는 문제였다면 안됐을것
# 꼭 시간 복잡도 먼저 생각하고 풀이해보기


# 변수 선언 및 입력:
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]
people_num = 0


# 탐색하는 위치가 격자 범위 내에 있는지 여부를 반환합니다.
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


# 탐색하는 위치로 움직일 수 있는지 여부를 반환합니다.
def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1


def dfs(x, y):
    global people_num

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # 네 방향에 각각에 대하여 DFS 탐색을 합니다.
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            # 마을에 존재하는 사람을 한 명 추가해줍니다.
            people_num += 1
            dfs(new_x, new_y)


# 가장 큰 마을의 크기를 구합니다.
def get_max_area():
    global people_num

    max_area = 0

    # visited 값을 초기화합니다.
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # 격자의 각 위치에서 탐색을 시작할 수 있는 경우
    # 한 마을에 대한 DFS 탐색을 수행합니다.
    for i in range(n):
        for j in range(n):
            if can_go(i, j):
                # 해당 위치를 방문할 수 있는 경우 visited 배열을 갱신하고
                # 새로운 마을을 탐색한다는 의미로 people_num을 1으로 갱신합니다.
                visited[i][j] = True
                people_num = 1

                dfs(i, j)

                # 한 마을에 대한 탐색이 끝난 경우 
                # 마을 내의 사람 수 중 최댓값을 갱신합니다.
                max_area = max(max_area, people_num)

    return max_area

   
# 모든 위치에 대해 
# 사람이 추가된다고 가정하는 
# 완전탐색을 진행합니다.
# 그 중 최댓값을 구해줍니다.
ans = 0
for i in range(n):
    for j in range(n):
        # 비어 있는 곳에 추가해봅니다.
        if grid[i][j] == 0:
            grid[i][j] = 1

            # 답을 갱신합니다.
            ans = max(ans, get_max_area())

            # 다시 상태를 되돌려줍니다.
            grid[i][j] = 0

print(ans)