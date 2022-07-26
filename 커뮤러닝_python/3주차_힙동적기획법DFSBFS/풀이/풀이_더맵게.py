import heapq
def solution(scoville, K):
    answer = 0
    # min heap
    heapq.heapify(scoville)
    
    while True:
        ## 탈출조건 
        # 모든 음식의 스코빌 지수 K이상
        # 모든 음식을 돌았을 때

        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break;
        elif len(scoville) == 0: 
            answer = -1
            break
        
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + 2 * min2

        heapq.heappush(scoville, new_scoville)
        answer += 1

    return answer