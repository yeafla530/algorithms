import heapq

n = int(input())
pq = []

for _ in range(n):
    num = int(input())

    if num == 0:
        if pq:
            x = heapq.heappop(pq)
            print(x)
        else:
            print(0)

    else:
        heapq.heappush(pq, num)
