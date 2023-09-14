import heapq

n = int(input())
arr = list(map(int, input().split()))
pq = []

for x in arr:
    heapq.heappush(pq, -x)

while len(pq) >= 2:
    n1 = -heapq.heappop(pq)
    n2 = -heapq.heappop(pq)
    if n1 == n2:
        continue
    
    else:
        heapq.heappush(pq, -abs(n1-n2))

if pq:
    print(-pq[0])
else:
    print(-1)