# 우선순위 큐
# 파라매트릭 서치

import sys
import heapq

si = sys.stdin.readline

n = int(si())
a = [list(map(int, si().split())) for _ in range(n)]

hw = [[] for _ in range(365)] # hw[i] := i일에 시작하는 과제 집합, (끝나는날, 필요한 시간)

# 각 날마다 출제되는 숙제들의 과제 집합 저장
for s, e, h in a:
    hw[s].append((e, h))

# 결정문제에 대한 풀이
def solve(X: int) -> bool: # 하루에 X시간씩 공부해서 모든 과제를 수행할 수 있는가?
    q = [] # 지금 할 수 있는 숙제들을 들고있는 우선순위 큐

    for day in range(365):
        for v in hw[day]: # day 일에 출제된 과제들을 우큐에 추가
            heapq.heappush(q, v)
        
        cnt = X # 오늘 내가 사용할 수 있는 시간
        while q and cnt > 0: # 숙제가 남아있고 && 사용할 수 있는 시간도 남아있음
            e, h = q[0]
            # 오늘이 day인데, 기한이 e였던 숙제
            if e < day: # 이미 기한을 넘은 숙제
                return False

            # 내가 사용할 수 있는 시간이 더 많으면
            if h <= cnt: # 해당 숙제를 다 끝내버릴 수 있다.
                cnt -= h
                heapq.heappop(q)
            
            else: #해당숙제 못끝냄
                q[0] = (e, h-cnt)
                cnt = 0

    # q가 비어있으면 성공, 아니면 실패
    return not q



# 파라매트릭서치
l, r, ans = 0, 1000000000, 1000000000
while l <= r:
    mid = (l + r) // 2
    if solve(mid):
        ans = mid
        r = mid - 1
    
    else:
        l = mid + 1


print(ans)


'''
4
0 1 4 
1 3 7
2 2 3
3 4 5

4
0 1 4  hw[0] (1, 4)
1 3 7  hw[1] (3, 7)
2 2 3  hw[2] (2, 3)
3 4 5  h2[3] (4, 5)
=>
4
'''