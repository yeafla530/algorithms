# 두 원소(a, b)의 합이 k라면
# k - a = b
# 원소의 범위와 k가 10^9이 되는 문제
# n, m도 10만까지,, 


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
a = set(a)
b = set(b)

for x in a:
    if k - x in b:
        ans += 1

print(ans)