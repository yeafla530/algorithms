# sort
n = int(input())
a = list(map(int, input().split()))

a.sort()

cnt = 1
num = a[0] 
result = 0
for i in range(1, n):
    if a[i] - num != 1:
        result = max(result, cnt)
        cnt = 1
        num = a[i]
        continue
    
    num = a[i]
    cnt += 1
result = max(result, cnt)
print(result)


# HASHSET 풀이
# 최대연속 부분수열
# 어떤 구간을 잡았을 때 연속되는 수들의 최대 구간을 구하는 문제
n = int(input())

arr = list(map(int, input().split()))

d = set(arr[:])
visited = set()

result = 0
# 자신의 양옆의 수가 있는지 확인
for i in range(n):
    if arr[i] in visited:
        continue
    cnt = 0

    curr_pre_num = arr[i]
    while curr_pre_num in d:
        if curr_pre_num in visited:
            break
        visited.add(curr_pre_num)
        cnt += 1
        curr_pre_num = curr_pre_num - 1
        # print("curr_pre_num", curr_pre_num)

    curr_nxt_num = arr[i]+1
    while curr_nxt_num in d:
        if (curr_nxt_num in visited):
            break
        visited.add(curr_pre_num)
        cnt += 1
        curr_nxt_num = curr_nxt_num + 1
        # print("curr_nxt_num", curr_nxt_num)

    
    # print(visited)
    result = max(result, cnt)

print(result)


        




    