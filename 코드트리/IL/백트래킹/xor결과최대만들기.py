## 추천 풀이
n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
def find_max(curr_idx, cnt, curr_val):
    global ans
    if cnt == m:
        ans = max(ans, curr_val)
        return

    if curr_idx == n:
        return 

    # 선택 안했을 경우
    find_max(curr_idx+1, cnt, curr_val)
    find_max(curr_idx+1, cnt+1, curr_val^arr[curr_idx])


find_max(0, 0, 0)
print(ans)


## 내가 생각했던풀이
n, m = map(int, input().split())
a = list(map(int, input().split()))
visited = [False for _ in range(n)]

ans = 0

def calc():
    selected_numbers = [
        a[i] for i in range(n) if visited[i]
    ]

    if m <= 1:
        return selected_numbers[0]

    num = selected_numbers[0] ^ selected_numbers[1]
    for i in range(2, m):
        num = num ^ selected_numbers[i]
    
    return num

def find_max_xor(curr_idx, cnt):
    global ans

    if cnt == m:
        ans = max(ans, calc())
        return    
    if curr_idx == n:
        return
    # curr_idx index에 있는 숫자 선택하지 않은 경우
    find_max_xor(curr_idx+1, cnt)
    visited[curr_idx] = True
    find_max_xor(curr_idx+1, cnt+1)
    visited[curr_idx] = False


find_max_xor(0, 0)
print(ans)