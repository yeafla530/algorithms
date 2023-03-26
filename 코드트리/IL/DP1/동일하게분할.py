# DP - 어렵다
import sys
n = int(input())
arr = [0] + list(map(int, input().split()))

m = sum(arr)

dp = [[False]*(m+1) for _ in range(n+1)]


def initialize():
    dp[0][0] = True

initialize()

for i in range(1, n+1):
    for j in range(m+1):

        if j >= arr[i] and dp[i-1][j-arr[i]]:
            dp[i][j] = True
        
        if dp[i-1][j]:
            dp[i][j] = True

ans = 'No'
for i in range(1, n+1):
    for j in range(1, m+1):
        if dp[i][j]:
            num1 = sum(arr) - j
            if num1 == j:
                ans = "Yes"

print(ans)



# backtracking 시간초과 
import sys

n = int(input())

arr = list(map(int, input().split()))

sum_num = []
visited = [False] * n
ans = "No"
def choose(num, cnt):
    global sum_num, visited
    if num == cnt:
        a = sum(sum_num)
        b = sum(arr) - a

        # print(a, b, sum_num)
        if a == b:
            print("Yes")
            # print("EEEE")
            sys.exit()
        
        return

    for i in range(n):
        if not visited[i]:
            sum_num.append(arr[i])
            visited[i] = True
            choose(num, cnt+1)
            sum_num.pop()
            visited[i] = False




for i in range(1, n+1):
    choose(i, 0)


print(ans)