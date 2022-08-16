import sys
n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]
MAX_INT = sys.maxsize
ans = MAX_INT
for i in range(1, n-1):
    dis = 0
    # prev 사용
    prev_idx = 0
    for j in range(1, n):
        if i == j:
            continue
        # 나의 풀이
        # if j == i+1:
        #     dis += abs(point[j-2][0]-point[j][0]) + abs(point[j-2][1] - point[j][1])

        # else:
        #     dis += abs(point[j-1][0]-point[j][0]) + abs(point[j-1][1] - point[j][1])
    # print(dis)
        dis += abs(point[prev_idx][0]-point[j][0]) + abs(point[prev_idx][1] - point[j][1])
        prev_idx = j
    
    ans = min(ans, dis)

print(ans)