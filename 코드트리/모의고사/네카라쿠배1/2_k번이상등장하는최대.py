# 내가 너무 어렵게 생각했음
# 완전탐색, hash로 풀 수 있음

n, k = map(int, input().split())
a = list(map(int, input().split()))

# n개의 수가 주어졌을 때 k번이상 등장하는 수 중 최대값

a.sort()

s = 0
e = 0
cur_num = a[0]
max_num = -1
for i in range(1, n):
    if cur_num == a[i]:
        if i == n-1:
            e = i
        e += 1
        continue
    else:
        e = i-1
        
    # print(s, e, e-s+1, cur_num)

    # k개 이상일 때
    if e - s + 1 >= k:
        # 최대값 찾기
        if cur_num > max_num:
            max_num = cur_num
    
    if i != n-1:
        s = i
        cur_num = a[i]

# print(s, e, e-s+1, cur_num)
if e-s+1 >= k:
    if cur_num > max_num:
        max_num = cur_num

print(max_num)


### hashmap 풀이
n, k = map(int, input().split())
a = list(map(int, input().split()))
freq = {}




for i in range(n):
    freq[a[i]] = freq.get(a[i], 0) + 1

result = -1
for key in freq.keys():
    # print(key, value)
    if freq[key] >= k:
        result = max(result, key)

print(result)





