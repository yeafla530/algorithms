import heapq
def solution(no, works):
    # 배상비용을 최소화
    # 배상비용 = 각 선반의 완성까지 남은 일의 작업량 ** 2 해서 모두 더한 값
    
    result = 0
    
    if (no > sum(works)):
        return 0    
    
    
    else:
        # heap은 기본적으로 가장 작은 값을 찾게 되어 있어 최대값을 찾으려고 하는 방식
        works = [(-i, i) for i in works]
        heapq.heapify(works)
        for _ in range(no):

            # 제일 값을 수 꺼낸다
            work = heapq.heappop(works)[1] - 1
            # 1을 뺀 값을 다시 push한다
            # 알아서 heap방식으로 push됨
            heapq.heappush(works, (-work, work))
            # print(works)
        
        
    


    return sum(i[1]**2 for i in works)