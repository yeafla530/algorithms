import heapq
n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    heapq.heappush(arr, num)

for i in range(n):
    print(heapq.heappop(arr))


