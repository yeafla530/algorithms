####### 위상정렬 특징
# 사이클이 없는 방향그래프여야함
# 여러가지 답이 존재할 수 있다
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단가능
# 스택을 활용한 DFS를 이용해 위상 정렬을 수행할수도 있음
# 시간복잡도 O(V+E)


####### 큐를 이용한 위상정렬 알고리즘 동작과정
# 1. 진입차수가 0인 모든 노드를 큐에 넣는다
# 2. 큐가 빌 때까지 다음 과정 반복
#     2-1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다
#     2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다

# => 결과적으로 각 노드가 큐에 들어온 순서가 위상정렬을 수행한 결과와 같다

from collections import deque

# 노드개수, 간선개수
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수 0 으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동가능
    # 진입 차수 1증가 
    indegree[b] += 1

# 위상정렬함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담은 리스트
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이되는 노드들 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()