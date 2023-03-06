# 내 풀이
n, k = map(int, input().split())
arr = list(map(int, input().split()))


ans = -1
d = {}

for i in range(n):
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1
    
    
    if d[arr[i]] >= k:
        ans = max(ans, arr[i])
print(ans)

# hashmap 풀이 
n, k = map(int, input().split())
arr = list(map(int, input().split()))
freq = {}

for i in range(n):
    freq[arr[i]] = freq.get(a[i], 0) + 1

result = -1
for key in freq.keys():
    result = max(result, key)

print(result)


