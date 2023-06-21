n, k = map(int, input().split())


storage = []
for _ in range(n):
    num, idx = map(int, input().split())
    storage.append([num, idx])

storage.sort(key=lambda x: x[1])

ans = 0
sum_val = storage[0][0]
j = 0

for i in range(0, n):
    while j + 1 < n and storage[j+1][1] - storage[i][1] <= 2*k:
        j += 1
        sum_val += storage[j][0]
        
    
    ans = max(ans, sum_val)

    sum_val -= storage[i][0]

print(ans)