import sys

si = sys.stdin.readline
N, B = map(int, si().split())
a = list(map(int, si().split()))

def slove(H: int) -> bool:
    # 모든 나무의 높이가 H 이상이도록 할 수 있는가? O(N)
    need = 0
    for x in a:
        if x >= H: # 이미 나무가 H이상이면, 비료 사용할 필요 없음
            continue
    
        need += (H - x) * (H - x)
    
    return need <= B

L, R, ans = 1, 2e9, 0 #(log 20억)
while L <= R:
    mid = (L + R) // 2
    if solve(mid):
        ans = mid
        L = mid + 1
    
    else:
        R = mid - 1
    

print(ans)