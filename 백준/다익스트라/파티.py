# 오고가는데 가장 많은 시간을 소비하는 학생 
# X마을에 모여 파티를 연다 

# 오고가는데 가장 많은 시간을 소비하는 학생
import heapq
import sys
INF = sys.maxsize

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[INF for _ in range(n+1)] for _ in range(n+1)] 

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start][start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[start][now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for i in range(1, n+1):
    dijkstra(i)

result = [0] * (n+1)
# print(graph)
for i in range(1, n+1):
    if i != x:
        result[i] += distance[i][x]
        continue
    for j in range(1, n+1):
        if j == x:
            continue
        result[j] += distance[i][j]
        

print(max(result))