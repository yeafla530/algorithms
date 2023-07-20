import heapq

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
pq = []


for _ in range(m):
    x, y = map(int, input().split())
    edges[x].append(y)
    indegree[y] += 1


for i in range(1, n+1):
    if not indegree[i]:
        heapq.heappush(pq, i)


while pq:
    x = heapq.heappop(pq)
    print(x, end=" ")
    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            heapq.heappush(pq, y)

