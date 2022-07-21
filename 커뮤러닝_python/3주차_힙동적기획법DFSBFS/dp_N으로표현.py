# 블로그 참고 풀이
# DP는 어려워,,,
def solution(N, number):
    anwer = 0
    if N == number:
        return 1
    # 1. [SET * 8] 초기화
    dp = [set() for _ in range(8)]
    
    # 2. set마다 기본 수 "N"*i 수 초기화
    for idx, x in enumerate(dp, start=1):
        x.add(int(str(N)*idx))

    # dp[0] = {5} : 1개의 N을 가지고 있는 경우
    for i in range(1, 8):
        for j in range(i): # 0 ~ i-1 까지
            for op1 in dp[j]: # j+1개 사용해서 만든 원소들
                for op2 in dp[i-j-1]: # 왜 i-j-1인가요?????
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

        if  number in dp[i]:
            print(dp[i], i)
            # dp[0] 0이 1개로 하는 경우이므로 +1 해줌  
            answer = i + 1
            break
    # print(dp)
        else:
            answer = -1
    return answer