from sortedcontainers import SortedSet

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet()
for elem in arr:
    if elem not in s:
        s.add(elem)
    

for _ in range(k):
    print(s[-1], end=" ")
    
    s.remove(s[-1])