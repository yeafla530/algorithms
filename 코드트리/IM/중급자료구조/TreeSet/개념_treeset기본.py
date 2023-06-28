from sortedcontainers import SortedSet

s = SortedSet([10, 15])
print(s)
print(s.bisect_left(9)) # 9보다 같거나 큰 최초 숫자 위치 0
print(s.bisect_left(10)) # 10보다 //                    0
print(s.bisect_left(11)) # 11보다 //                    1
print(s.bisect_left(16)) # 16보다 //                    2
print(s.bisect_left(17)) # 16보다 //                    2


idx = s.bisect_left(9)   # 9보다    //                  0
print(s[idx])            # 9보다 같거나 큰 최초 숫자 값10



print(s.bisect_right(9))  # 9보다 큰 최초 숫자의 위치 = 0
print(s.bisect_right(10)) # 10보다 큰 최초 숫자의 위치 = 1
print(s.bisect_right(11)) # 11보다 큰 최초 숫자의 위치 = 1
print(s.bisect_right(16)) # 16보다 큰 최초 숫자의 위치 = 2

idx = s.bisect_right(10)  # 10보다 큰 최초 숫자의 위치 = 1
print(s[idx])             # 10보다 같거나 큰 최초 숫자 값 = 15