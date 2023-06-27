# 전 동전의 가치의 배수
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# 동전개수 최소개수 구하기
ans = 0

# 큰 동전부터 놓는게 유리
for coin in coins[::-1]:
    ans += k // coin
    k = k % coin

print(ans)