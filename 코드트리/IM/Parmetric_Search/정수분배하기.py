n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

left = 1 # 최소 시작점
right = 100001 # 최대 시작점
k = 0 # 답

def is_possible(max_num):
    global k
    count = 0

    for elem in arr:
        count += elem // max_num

    
    if count >= m:
        k = max_num
        return True
    
    else:
        return False


while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
    else:
        right = mid - 1

print(k)

