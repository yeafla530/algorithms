# 내 풀이 : 시간 초과

import sys
from collections import deque

INT_MAX = sys.maxsize

# y좌표 차가 D이상 
n, d = map(int, input().split())

# x좌표가 특정 범위안에 있는 점들 중 y좌표 가장 작은 점과 가장 큰 두점이 D이상이 되도록 만들려고 한다
# x좌표 범위가 A <= x <= B라고 했을 때 B-A가 최소가 되게 만드는 프로그램

ans = INT_MAX
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort(key=lambda x: x[0])
# print(arr)
# i, j 는 x좌표
j = 0

q = deque()
q.append(arr[0][1])
y_min = min(q)
y_max = max(q)

for i in range(n):
    if j >= n-1:
        break
    if i > 0:
        q.popleft()
        y_min = min(q)
        y_max = max(q)

    
    while j + 1 < n and y_max - y_min < d:
        j += 1
        # print(j)
        q.append(arr[j][1])
        y_min = min(q)
        y_max = max(q)

    # print(i, j, y_min, y_max, y_max - y_min, arr[j][0] - arr[i][0])
    if j <= n-1 and y_max - y_min >= d:
        ans = min(ans, arr[j][0] - arr[i][0])
    
        # print(ans)

if ans == INT_MAX:
    print(-1)
else:
    print(ans)


### 풀이 정답

# 1. sortedSet인 TreeSet을 사용해 O(logN)시간 * O(logN) 걸림
# 2. 삭제를 초반에 하는게 아닌 다 끝나고 진행 (아주 굳)
import sys
from sortedcontainers import SortedSet

INT_MAX = sys.maxsize

n, d = map(int, input().split())
point = [tuple(map(int, input().split())) for _ in range(n)]

point = [(0, 0)] + sorted(point)

# 변수 선언
point_count = SortedSet()

def get_min():
    if not point_count:
        return 0
    
    return point_count[0][0]

def get_max():
    if not point_count:
        return 0
    
    return point_count[-1][0]

ans = INT_MAX


# 구간 잡기
j = 0

for i in range(1, n+1):
    # y좌표 차가 d가 되기 전까지 계속 진행
    while j + 1 <= n and get_max() - get_min() < d:
        point_count.add((point[j+1][1], point[j+1][0]))
        j += 1
    
    # 만약 최대한 이동했는데도 y좌표차가 d가 되지 못한다면 종료
    if get_max() - get_min() < d:
        break

    ans = min(ans, point[j][0] - point[i][0])

    # 다음 구간 넘어가기 전에 
    # point[i]에 해당하는값 point_cout에서 삭제
    point_count.remove((point[i][1], point[i][0]))



if ans == INT_MAX:
    print(-1)

else:
    print(ans)