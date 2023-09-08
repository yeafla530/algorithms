# 2명의 신입사원이 같이 공부하면 서로의 능력을 흡수하여 두 신입사원의 능력치는 공부 전 두 사람의 능력치의 합이 됨
# 3과 7인 두 사원이 같이 공부하면 두 사원의 능력치가 모두 10
# 모든 신입사원의 능력치 합을 최소화

import heapq

def solution(ability, number):
    answer = 0
    
    cnt = 0
    heap = []
    for elem in ability:
        heapq.heappush(heap, elem)
        
    while cnt != number:
        cnt += 1
        
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)


        s = num1 + num2
        heapq.heappush(heap, s)
        heapq.heappush(heap, s)
            
        
    
    
    return sum(heap)