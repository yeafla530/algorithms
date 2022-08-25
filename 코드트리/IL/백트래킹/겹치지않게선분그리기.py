# 겹치지 않게 가장 많은 수의 선분 고르는 프로그램
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
selected = []

def overlapped(seg1, seg2):
    (ax1, ax2), (bx1, bx2) = seg1, seg2
    return (ax1 <= bx1 <= ax2) or (ax1 <= bx2 <= ax2) or (bx1 <= ax1 <=bx2) or (bx1 <= ax2 <= bx2)

def possible():
    for i, seg1 in enumerate(selected):
        for j, seg2 in enumerate(selected):
            if i < j and overlapped(seg1, seg2):
                return False
    return True

# 겹치지 않게 선분 고르기
def find_max_segment(cnt):
    global ans
    if cnt == n:
        if possible():
            ans = max(ans, len(selected))
        return

    # 포함시키기
    selected.append(arr[cnt])
    # print(selected)
    find_max_segment(cnt+1)
    selected.pop()

    # 아무것도 안하기
    find_max_segment(cnt+1)



find_max_segment(0)


print(ans)