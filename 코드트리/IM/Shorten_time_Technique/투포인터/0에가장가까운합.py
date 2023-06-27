import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

arr = [0] + sorted(arr)

ans = INT_MAX
j = n

for i in range(1, n+1):
    if i < j:
        ans = min(ans, abs(arr[i] + arr[j]))
    
    # j가 왼쪽으로 이동할수록 수는 줄어든다
    # a[i] + a[j]가 음수라면, j가 왼쪽으로 이동시에도 음수인경우 함의 절대값은 줄어들것이다
    # -100 10 20 30 인경우에 abs(-100 + 30) = 70   / abs(-100 + 20) = 80
    # 그래서 a[i] + a[j]가 양수일때 더해주는것
    while i < j-1 and arr[i] + arr[j] > 0:
        j -= 1
        ans = min(ans, abs(arr[i] + arr[j]))
    

print(ans)