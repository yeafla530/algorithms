# 두자리 숫자 중 3의 배수는 아니면서 십의 자리 숫자와 일의 자리 숫자가 다른 수 => 개수세기
def is_magin_number(n):
    return n%3 != 0 and all_different(n)

def all_different(n):
    return (n//10) != (n%10)
cnt = 0
for i in range(10, 100):
    # 3의 배수 아니면서
    # 각 자리에 있는 숫자가 다른 경우
    if is_magin_number(i):
        cnt += 1



print(cnt)