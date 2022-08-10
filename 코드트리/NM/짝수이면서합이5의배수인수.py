# 짝수면서 각자리 숫자 합이 5의 배수
def magic_number(n):
    return n % 2 == 0 and  (n // 10 + n % 10) % 5 == 0

n = int(input())
if magic_number(n):
    print("Yes")
else:
    print("No")