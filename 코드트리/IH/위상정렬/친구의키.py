# n개의 노드, m개의 간선
n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
visited = [False] * (n+1)
reversed_order = []


for _ in range(m): 
    a, b = map(int, input().split())
    edges[a].append(b)

def dfs(x):
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            dfs(y)

    reversed_order.append(x)



for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        dfs(i)

for num in reversed_order[::-1]:
    print(num, end=" ")



# in-degree
from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
q = deque()

for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    indegree[y] += 1


for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)


while q:
    x = q.popleft()

    print(x, end=" ")

    for y in edges[x]:
        indegree[y] -= 1
        
        if not indegree[y]:
            q.append(y)            


