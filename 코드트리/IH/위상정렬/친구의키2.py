from collections import deque 

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
q = deque()
cnt = 0

for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    indegree[y] += 1

for i in range(1, n+1):
    if not indegree[i]:
        q.append(i)


while q:
    x = q.popleft()
    cnt += 1

    for y in edges[x]:
        indegree[y] -= 1
        if not indegree[y]:
            q.append(y)


if cnt == n:
    print("Consistent")

else:
    print("Inconsistent")