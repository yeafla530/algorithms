def solution(n, info):
    answer = [0] * 11
    # 라이언 점수표
    tmp = [0] * 11
    maxDiff = 0
    
    # 2진수로 1~1023까지
    # 0000000001 ~ 1111111111
    # 이기게 만들 점수
    for subset in range(1, 1 << 10):
        ryon = 0
        apeach = 0
        cnt = 0
        
        # 10 9 8 7 6 5 4 3 2 1
        for i in range(10):
            # 10~1점순으로 돌면서 
            # 라이언이 이겨서 얻을 점수를 계산해준다
            if subset & (1 << i):
                ryon += 10 - i
                tmp[i] = info[i] + 1
                cnt += tmp[i]
            # 라이언이 해당 과녁을 안쏘는 경우
            else:
                tmp[i] = 0
                # 어피치가 이기는 경우
                if info[i]:
                    apeach += 10 - i
        
        # 라이언이 사용한 화살이 더 많으면 넘어감
        if cnt > n: continue
        
        # 유효한 경우
        # 화살이 남는 경우 : 
        # 전체 화살에서지금까지 쏜 화살을 빼준다
        tmp[10] = n - cnt
        
        # 최대 점수차 여러가지인 경우
        # 낮은 점수를 더 많이 맞힌경우 return
        if ryon - apeach == maxDiff:
            # 0점부터 비교
            for i in reversed(range(11)):
                if tmp[i] > answer[i]:
                    maxDiff = ryon - apeach
                    answer = tmp[:]
                    break
                elif tmp[i] < answer[i]:
                    break
            
        
        # 라이언이 이기는데 최대 점수차로 이기는 경우
        elif ryon - apeach > maxDiff:
            maxDiff = ryon - apeach
            answer = tmp[:]
            
    if maxDiff == 0:
        answer = [-1]
    
    
    return answer

