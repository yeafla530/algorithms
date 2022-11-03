n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * (n+1)
result = []

for i in range(n):
    prefix[i+1] = arr[i] + prefix[i] 

for _ in range(m):
    s, e = map(int, input().split())

    result.append(prefix[e] - prefix[s-1])


for r in result:
    print(r)
