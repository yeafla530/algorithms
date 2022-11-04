import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선개수 입력받기
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드에 연결되어있는 노드에 대한 정보 담는 리스트
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번노드에서 b번노드로 가는 비용 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
    
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distnace[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])




