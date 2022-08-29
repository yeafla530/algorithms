MAX_INT = 45
n = int(input())
memo = [-1] * (MAX_INT + 1)

def fibo(n):
    # 이미 계산된 값이면
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        return 1


    memo[n] = fibo(n-1) + fibo(n-2)  
    return memo[n]

print(fibo(n))