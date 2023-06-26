# 서로 다른 2개 위치 골라 해당 위치에 적혀있는 수들의 합이 0에 가장 가깝게 만들기
import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

arr = [0] * sorted(arr)

# 0에 가장 가까운 합 구하기
ans = INT_MAX

j = n
for i in range(1, n+1):
    
    if i < j:
        ans = min(ans, abs(arr[i] + arr[j]))
    
    # 두 수의 합이 0이하가 될때까지 j구간 내리면서 정답 살피기
    while i < j - 1 and arr[i] + arr[j] > 0:
        j -= 1
        ans = min(ans, abs(arr[i] + arr[j]))

print(ans)

    
