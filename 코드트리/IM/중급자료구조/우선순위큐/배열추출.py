import heapq

n = int(input())
pq = []

for _ in range(n):
    x = int(input())
    heapq.heappush(pq, -x)

    if x == 0:
        print(-1* heapq.heappop(pq))

# 정답 풀이
import heapq

n = int(input())
arr = [int(input()) for _ in range(n)]

pq= []

for x in arr:
    if x != 0:
        heapq.heappush(pq, -x)

    # 0이 아니면
    else:
        # 비어있다면
        if not pq:
            print(0)
        
        else:
            print(-heapq.heappop(pq))


