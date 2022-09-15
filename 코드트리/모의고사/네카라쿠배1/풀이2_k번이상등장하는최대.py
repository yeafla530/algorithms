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