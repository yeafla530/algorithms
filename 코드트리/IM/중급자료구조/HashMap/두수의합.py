n, k = map(int, input().split())
d = {}
arr = list(map(int, input().split()))
ans = 0

for i in range(n):
    num = arr[i]
    if k-num in d:
        ans += d[k-num]
    
    
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
     
    
    
    

print(ans)
    