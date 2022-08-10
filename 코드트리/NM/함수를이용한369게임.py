# a이상 b이하 수들중 3 6 9 중 하나가 들어가있거나 숫자 자체가 3의 배수인 숫자

def magic_number(n):
    return n % 3 == 0 or is_369(n)

def is_369(n):
    n = str(n)
    for i in range(len(n)):
        if n[i] in '3' or n[i] in '6' or n[i] in '9':
            return True
    return False

a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    # 369 들어있거나
    # 숫자 자체가 3의 배수 
    if magic_number(i):
        cnt += 1
print(cnt)


    