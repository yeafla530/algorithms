# 나의 풀이 - 복잡하게 풀었음
import copy
n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
m_arr = list(map(int, input().split()))

cnt = 0
for i in range(n-m+1):
    del_arr = copy.deepcopy(m_arr)
    for j in range(i, i+m):
        # print(n_arr[j], j)
        if n_arr[j] in del_arr:
            find_idx = del_arr.index(n_arr[j])
            del_arr.pop(find_idx)
    
    if len(del_arr) == 0:
        cnt += 1

print(cnt)


# 정답풀이 - sorted이용
import copy
n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
m_arr = list(map(int, input().split()))

cnt = 0
for i in range(0, n-m+1):
    if sorted(n_arr[i:i+m]) == sorted(m_arr):
        cnt += 1

print(cnt)