# 수와 수를 더했을 때 10의 자리를 넘기는 것
# 각 자리수 모두 더해봤을 때 10이상이 되는 경우가 전혀 없어야함
n = int(input())
arr = [int(input()) for _ in range(n)]

# arr 만큼 for
ans = -1
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            carry = False
            # 1의자리
            if arr[i] % 10 + arr[j] % 10 + arr[k] % 10 >= 10:
                continue
            # 10의자리
            if arr[i] % 100 // 10 + arr[j] % 100 // 10 + arr[k] % 100 // 10 >= 10:
                continue
            # 100의 자리
            if arr[i] % 1000 // 100 + arr[j] % 1000 // 100 + arr[k] % 1000 // 100 >= 10:
                continue
            if arr[i] % 10000 // 1000 + arr[j] % 10000 // 1000 + arr[k] % 10000 // 1000 >= 10:
                continue
            
            ans = max(ans, arr[i]+arr[j]+arr[k])

print(ans)
            
            





