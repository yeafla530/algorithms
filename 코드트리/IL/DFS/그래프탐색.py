n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] *(n+1)
for _ in range(m):
    x, y = map(int, input().split())
    

    graph[x].append(y)
    graph[y].append(x)

ans = 0

def dfs(v):
    global ans
    for num in graph[v]:
        if not visited[num]:
            visited[num] = True
            ans += 1
            dfs(num)



visited[1] = True
dfs(1)
print(ans)

# 인접 행렬
# n이 1000이어서 괜찮다
n, m = map(int, input().split())

graph = [[0]*n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] * (n)

ans = 0

def dfs(v):
    global ans
    for i in range(n):
        if graph[v][i] and not visited[i]:
            visited[i] = 1
            ans += 1
            dfs(i)

visited[0] = 1
dfs(0)
print(ans)
