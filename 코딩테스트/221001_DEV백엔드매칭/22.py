from collections import deque

def solution(maps):
    answer = 0
    # ABCEKLMQTXT
    # 가장 넓은 영토 가진 나라 여러개면 알파벳 순서가 가장 뒤인 나라가 승
    # 승리한 나라는 자기보다 영토가 작은나라 점령
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    q = deque()
    

    graph = [['']*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            graph[i][j] = maps[i][j] 
            
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    def can_go(x, y):
        return in_range(x, y) and (not visited[x][y]) and (graph[x][y] != '.')

    # 같은 영역 찾기
    def bfs():
        x_y = []
        country = {}
        x_y.append((q[0][0], q[0][1]))
        while q:
            x, y = q.popleft()
            country[graph[x][y]] = country.get(graph[x][y], 0) + 1 
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if can_go(nx, ny):
                    q.append((nx, ny))
                    x_y.append((nx, ny))
                    visited[nx][ny] = True


        # 지배하는 나라 찾기 
        c = []
        value = 0
        # print(country)
        for x in country.keys():
            value = max(value, country[x])

        for x in country.keys():
            if country[x] == value:
                c.append(x)

        if len(c) > 1:
            c.sort()
            best = c[-1]
        else:
            best = c[0]

        # 지배될 영역 바꾸기
        for x, y in x_y:
            if graph[x][y] not in c:
                graph[x][y] = best


    # 출발지 찾기
    for x in range(n):
        for y in range(m):
            if can_go(x, y):
                q.append((x, y))
                visited[x][y] = True
                bfs()

    # 개수 찾기
    d = {}
    for i in range(n):
        for j in range(m):
            if graph[i][j] != '.':
                d[graph[i][j]] = d.get(graph[i][j], 0) + 1
    
    for k, v in d.items():
        answer = max(answer, v)


    return answer


    return answer