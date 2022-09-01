yMOD = 10007
MAX_INT = 1000

n = int(input())
memo = [0] * (MAX_INT+1)

memo[0] = 1
memo[1] = 1

for i in range(2, n+1):
    memo[i] = (memo[i-1] + memo[i-2]) % MOD

# print(memo)
print(memo[n])


