n = int(input())
for _ in range(n):
    num = int(input())
    dp = [0] * 10001

    dp[0] = 1
    numbers = [1, 2, 3]
    for i in range(1, num+1):
        for j in range(3):
            if i >= numbers[j]:
                dp[i] = (dp[i] + dp[i - numbers[j]])
        
    
    print(dp[num])