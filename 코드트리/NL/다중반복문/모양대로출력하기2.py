n = int(input())


cnt = 1
for i in range(n):
    for j in range(n):
        print(2*cnt, end=" ")
        
        if cnt > 3:
            cnt = 1
        else:
            cnt += 1
    print()