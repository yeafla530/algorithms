import heapq

n, m = map(int, input().split())
pq = []

for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(pq, ((abs(x)+abs(y)), x, y))


for _ in range(m):
    num, x, y = heapq.heappop(pq)
    x += 2
    y += 2
    num = abs(x) + abs(y)

    heapq.heappush(pq, (num, x, y))

_, x, y = pq[0]

print(x, y)
