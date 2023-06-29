# TIL

## 0628

### TreeSet

* 트리셋은 완전한 이진트리로, 최대, 최소값을 찾을 때 편리하다

* 현재까지의 최대값을 O(logN) 시간복잡도로 구할 수 있다 => 총 O(NlogN)

* `from sortedcontainers import SortedSet` 을 통해서 TreeSet 을 불러올 수 있다

* 명령어

  ```
  from sortedcontainers import SortedSet`
  
  s = SortedSet()
  
  # 1. add
  s.add(1)
  
  # 2. remove
  s.remove(1)
  
  # 3. find
  s.find(1)
  
  # 4. bisect_left - 크거나 같은값
  s.bisect_left(1)  # 0
  
  # 5. bisect_right - 큰값
  s.bisect_right(2) # 1
  
  # 6. index값 이용해서 찾기
  idx = s,bisect_left(1)
  print(s[idx]) # 1
  
  # 7. E in s
  true if 1 in s else false 
  ```

  