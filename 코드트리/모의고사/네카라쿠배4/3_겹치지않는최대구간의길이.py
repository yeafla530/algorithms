
n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(n):
    h = set()

    for j in range(i, n):
        if arr[j] in h:
            break
        
        h.add(arr[j])

    result = max(result, len(h))



print(result)


#### 투포인터
n = int(input())
arr = [0] + list(map(int, input().split()))
ans = 0
s = {}

j = 0
for i in range(1, n+1):
    while j + 1 <= n and s.get(arr[j+1], 0) != 1:
        s[arr[j+1]] = s.get(arr[j+1], 0) + 1
        j += 1
    
    ans = max(ans, j-i+1)
    s[arr[i]] -= 1

print(ans)