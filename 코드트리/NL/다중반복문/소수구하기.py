n = int(input())

for i in range(2, n+1):
    # 소수 구하기
    isprime = True
    for j in range(2, i):
        if i % j == 0:
            isprime = False
            break

    if isprime:
        print(i, end=" ")
    