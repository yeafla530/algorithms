import sys 
from collections import defaultdict

si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))    # a: 원래배열 
s = [0] * n                         # s: 기존 누적합
zero = [0] * n                      # zero[i] := s[0...i]에 0이 등장하는 횟수

# s랑 zero배열을 계산
for i in range(n):
    s[i] = a[i]
    if i >= 1:
        s[i] += s[i-1]
        zero[i] = zero[i-1]

    if s[i] == 0:   
        zero[i] += 1

print(s)
# 아무것도 0으로 바꾸지 않은 경우에 대한 정답 갱신
ans = zero[n-1]

mem = defaultdict(int)          # mem[k] := 누적합 배열 s에 k라는 값이 등장한 횟수

# 하나씩 0으로 바꿔주기
for i in range(n-1, -1, -1):    # i번지에 있는 원소를 0으로 바꿔볼 차례
    mem[s[i]] += 1 # s[i]라는 새로운 누적합값이 등장했으니 mem에 반영

    v = 0   # i번째 원소를 0으로 바꾼 이후에 전체 누적합 배열의 0개수
    if i >= 1: 
        v = zero[i-1] # i번째 원소의 왼쪽은 누적합 배열이 그래도 유지
    
    print(v, mem[a[i]], a[i], mem)
    v += mem[a[i]] # 이번에 새롭게 0으로 계산되는 개수 
    print(v)
    ans = max(ans, v)

print(ans)

