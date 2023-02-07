n = int(input())


for i in range(n):
    cnt = 0
    a = int(input())
    
    
    while a != 1:
        if a % 2 == 0:
            a /= 2
        else:
            a = 3 * a + 1

        cnt += 1

    print(cnt)