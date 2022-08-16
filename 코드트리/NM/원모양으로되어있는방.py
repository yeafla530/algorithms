# 몇명의 사람이 들어가야하는지 주어짐
# 모든 사람이같은 방에서 시작
# 어떤방에서 시작해야각방에 정해진인원들어가고, 그 거리의 합의 최소 출력
import sys
n = int(input())
arr = list(int(input()) for _ in range(n))
INT_MAX = sys.maxsize

ans = INT_MAX
for start in range(n):
    sum_dist = 0 
    for i in range(n):
        dis = 0
        if i == start:
            continue
        
        dis = abs(i + n - start) % n
        # print(i, arr)
        sum_dist += arr[i] * dis

    ans = min(ans, sum_dist)

print(ans)