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

##### 2중 for문 풀이 => 시간 초과 
### 값을 기준으로 완전탐색 문제 공부하기
# 시간복잡도 O(N^2)
# 1억 = 1초
# 10만 제곱 = 100억 => 시간초과



##### hash map 풀이
# for 문을 한번 더 도는것은 비효율적
# key-value 사용
# IM의 HashMap 풀기
# 전처리 진행 : Preprocessing
freq = {}
# print(freq[4]) # error

for elem in arr:
    # 우리가 기대하는 값 안나옴 
    freq[elem] = freq[elem] + 1

    # 처음엔 이렇게 많이 작성
    if elem in freq:
        freq[elem] = freq[elem] + 1
    else:
        freq[elem] = 1

    # get 사용
    # get(key, default) => key값이 비어있으면 default로 반환해줌
    freq[elem] = freq.get(elem, 0) + 1

# 해결법 1: defaultdict 사용하면 
from collections import defaultdict
freq = defaultdict(lambda: 0) # 비어있으면 0으로 초기화 해준다는 뜻


###### count 배열처럼 하면 메모리 초과 => 10의 9승이기 때문에
###### 그래서 HashMap

# 배열크기가 2000만 넘으면 잘못 생각한것임



print(max_num)




