n, m = map(int, input().split())
a = list(map(int, input().split()))

prefix = [0] * n

prefix[0] = a[0]

for i in range(1, n):
    prefix[i] = prefix[i-1] + a[i]

result = 0
for i in range(n-m):
    result = max(result, prefix[i+m] - prefix[i])
print(result)