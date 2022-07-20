# 가장 맵지않은 음식을 뽑기위해 heap사용
import heapq
def solution(scoville, K):
    # 모든 음식의 스코빌 지수를 K이상으로 
    # 가장 낮은 두개 음식을 아래 방법으로 섞어 만듦
    # K가 될때까지 섞음
    # 최소 횟수 return
    answer = 0
    # 최소 heap으로 변환
    heapq.heapify(scoville)
    
    # 가장 작은값이 K보다 같거나 클때까지 반복
    while scoville[0] < K and len(scoville) > 1:
        answer += 1
        # 가장 안매운 스코빌
        first = heapq.heappop(scoville)
        # 두번째로 안매운 스코빌
        second = heapq.heappop(scoville)
        # print(first, second)
        # 계산식
        sum_scoville = first + (second * 2)
        heapq.heappush(scoville, sum_scoville)
        # print(scoville)
    
    # 모든 음식의 스코빌 지수 K이상으로 만들 수 없는 경우엔 -1
    if len(scoville) <= 1 and scoville[0] < K:
        return -1
    return answer