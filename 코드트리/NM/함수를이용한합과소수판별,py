def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def is_even(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    
    if s % 2 == 0:
        return True
    else:
        return False


a, b = map(int, input().split())

# 소수면서
# 모든 자리 합이 짝수
cnt = 0
for i in range(a, b+1):
    if is_prime(i) and is_even(i):
        cnt += 1

print(cnt)