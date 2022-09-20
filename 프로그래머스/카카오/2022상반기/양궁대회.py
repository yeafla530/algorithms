import sys
# Recursion Error 방지- 재귀의 한도 10000까지 풀어주기
sys.setrecursionlimit(10**7)

def solution(n, info):
    answer = []
    # 어피치가 화살 n발을 다 쏜 후에 라이언이 화살 n발을 쏨
    # 점수계산 
        # k점수에 맞춘 화살 횟수가 a > b인 경우 a가 k점을 가져감
        # a == b인경우 어피치가 k점 가져감
        # k점 여러개 맞추면 k점만 가져감
        # a = b = 0인경우, 누구도 k점을 가져가지 않음
    # 최종점수
        # 같을 경우 어피치가 우승
    # 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 
    # 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요. 
    
    # 어피치가 쏜 과녁의 점수개수 = 10점부터 0점까지 순서대로 담은 info
    # 라이언이 가장 큰 점수차이로 우승하기 위해 n발의 화살을 어떤 과녁점수에 맞혀야 하는지 10점부터 0점가지 담기
    
    # 라이언이 우승할 방법이 없는 경우 return할 정수배열의 길이는 1
    # 라이언이 어떻게 화살을 쏘든 라이언의 점수가 어피치의 점수보다 낮거나 같으면 [-1]을 return 해야 합니다.
    lion = [0] * 11
    # 이길 수 있는 경우로 초기화
    for i in range(len(info)):
        lion[i] = info[i] + 1
    
    apeach = sum(info)
    d = {}
    # 화살개수가 n개가 되게 하는 조합
    # 백트레킹?
    
    s = apeach
    def sum_score(score, idx, arrow_n):
        nonlocal s
        print(d)
        if arrow_n > n:
            return
        if arrow_n == n:
            s = max(s, score)
            
            print(s, d)
            return
        
        d[idx] = d.get(idx, 0) + lion[idx]
        sum_score(score+(10-idx), idx+1, arrow_n+lion[idx])
        d[idx] = d.get(idx, 0) - lion[idx]
        
        
        
    sum_score(0, 0, 0)
    # print(d)
    return answer

