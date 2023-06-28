# 숫자들 중 최댓값을 계속 구해주는 과정을 빠르게 할 수 있도록 도와주는 자료구조는 바로 treeset 
# treeset을 이용하면 최댓값을 찾는 과정을 O(logN)에 할 수 있습니다.
# 따라서 총 시간복잡도가 O(NlogN)이 됩니다.

from sortedcontainers import SortedSet

t = int(input())

for _ in range(t):
    k = int(input())
    s = SortedSet()
    for _ in range(k):
        arr = list(input().split())
        if arr[0] == "I":
            s.add(int(arr[1]))
        
        elif arr[0] == "D":
            if s:
                if arr[1] == '1':
                    s.remove(s[-1])
                else:
                    s.remove(s[0])

    if s:
        print(s[-1], s[0])
    else:
        print("EMPTY")
