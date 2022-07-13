import heapq
def solution(scoville, K):
    # 모든 음식의 스코빌 K이상
    # 지수가 가장 낮은 두개 음식을 섞어서 새로운 음식 만듦
    answer = 0
    heapq.heapify(scoville)
    
    while (len(scoville) > 1):
        if (scoville[0] >= K):
            return answer
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)

            heapq.heappush(scoville, first + (second*2))
            answer += 1 
    if (len(scoville) <= 1 and scoville[0] < K):
        return -1
    
    return answer