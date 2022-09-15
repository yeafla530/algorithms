# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

freq = [0] * (10**9) # 메모리초과
#print(freq[4])

# 전처리 : Preprocessing
# HashMap을 이용하여
# 각 수들이 몇 번씩 나왔는지를 세줍니다.
for elem in arr:
    freq[elem] = freq[elem] + 1
    
    # freq[elem] = freq[elem] + 1
    # freq[4] = freq[4] + 1

"""
freq[4] = 1
freq[1] = 2
freq[2] = 2
"""

# k번 이상 등장한 수 중 최댓값을 계산합니다. O(N)
ans = -1
for elem in arr:
    if freq[elem] >= k: # O(1)
        ans = max(ans, elem)

print(ans)


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
