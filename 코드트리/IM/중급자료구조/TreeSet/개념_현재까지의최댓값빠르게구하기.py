# 숫자들 중 최댓값을 계속 구해주는 과정을 빠르게 할 수 있도록 도와주는 자료구조는 바로 treeset 
# treeset을 이용하면 최댓값을 찾는 과정을 O(logN)에 할 수 있습니다.
# 따라서 총 시간복잡도가 O(NlogN)이 됩니다.

from sortedcontainers import SortedSet

arr = [3, 6, 2, 6, 7, 7, 2]
s = SortedSet()

for elem in arr:
    s.add(elem)
    print(s[-1], end=" ") # 3 6 6 6 7 7 7


