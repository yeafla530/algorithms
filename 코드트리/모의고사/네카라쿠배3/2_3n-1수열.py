n = int(input())
check = set()

cnt = 0
while n != 1:
    
    if n % 2 == 0:
        n //= 2
    
    else:
        n = 3 * n - 1

    # if 순서 중요ㅁ
    if n in check:
        cnt = -1
        break
    check.add(n)
    # print(check)
    cnt += 1

print(cnt)