def solution(triangle):
    # 거쳐간 숫자의 합이 가장 큰 경우
    # 대각선으로만 이동가능
    # 거쳐간 숫자의 최대값 return
    answer = 0
    dp = [set() for _ in range(len(triangle))]
    dp[0].add(triangle[0][0])
    # 그 다음부터는 x, x+1더해줌
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i].add(triangle[i][j] + triangle[i-1][j])
            elif j == len(triangle)-1:
                dp[i].add(triangle[i][j] + triangle[i][j-1])
            else:
                dp[i].add(triangle[i][j] + triangle[i][j-1])
                dp[i].add(triangle[i][j] + triangle[i][j])
        
    print(dp)
    
    return answer