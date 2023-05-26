MAX_S = 10**9
# 1부터 n까지의 자연수 합이 s이하인 경우 가능한 n의 최대값
s = int(input())

left = 1
right = MAX_S
max_num = 0 # 최대값 

while left <= right:
    mid = (left + right) // 2
    if mid * (mid+1) // 2 <= s:
        left = mid + 1
        max_num = max(max_num, mid)
    else:
        right = mid - 1


print(max_num)
