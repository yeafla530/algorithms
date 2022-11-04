# 다익스트라
# N개의 도시 각 도시에는 보내고자 하는 메시지가 있다 
# 다른 도시로 전보를 보내서 다른 도시로 전송가능
# C도시에서 출발하여 각 도시 사이에 설치된 통로를 통해 최대한 많이 퍼져나감
# C에서 보낸 메시지를 받는 도시의 개수는 총 몇개며 걸리는 시간은?
import heapq
INF = 987654321
# 도시의 개수, 통로의 개수, 메시지 보내고자 하는 도시 C
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

time = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0

    while q:
        t, now = heapq.heappop(q)

        if time[now] < t:
            continue
            
        for i in graph[now]:
            cost = t + i[1]
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
        

dijkstra(c)

count = 0
max_distance = 0

for t in time:
    if t != INF:
        count += 1
        max_distance = max(max_distance, t)

print(count-1, max_distance)