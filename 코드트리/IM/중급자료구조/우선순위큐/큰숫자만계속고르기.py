import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pq = []

for elem in arr:
    heapq.heappush(pq, -elem)

for _ in range(m):
    num = heapq.heappop(pq)
    num += 1
    heapq.heappush(pq, num)

print(-pq[0])