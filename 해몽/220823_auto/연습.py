import sys
from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
s = [0] * n
zero = [0] * n # i번째까지 n개의 개수

for i in range(n):
    s[i] = arr[i]

    if i >= 1:
        s[i] += s[i-1]
        zero[i] = zero[i-1]

    if s[i] == 0:
        zero[i] += 1 


ans = zero[n-1] # 제일 끝에 누적된 n개의 개수

mem = defaultdict(int)

for i in range(n-1, -1, -1):
    mem[s[i]] += 1 # 누적합 개수 count

    v = 0
    if i >= 1:
        v = zero[i-1] # 이전까지 0의 개수
    
    v += mem[arr[i]]
    ans = max(ans, v)

print(ans)



