def solution(N, stages):
    answer = []
    # 스테이지 도달했으나 클리어 못한 플레이어 / 스테이지 도달한 플레이어수
    # 실패율이 높은 스테이지부터 내림차순으로 
    num = len(stages)
    d = []
    for i in range(1, N+1):
        count = stages.count(i)
        if num != 0:
            d.append([i, (count / num)])
        else:
            d.append([i, 0])
        num -= count
    
    d.sort(key = lambda x: (-x[1], x[0]))
    for a in d:
        answer.append(a[0])
    
    return answer