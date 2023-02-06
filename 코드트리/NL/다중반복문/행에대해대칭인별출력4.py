n = int(input())

cnt = n

for i in range(n*2-1):
    for j in range(cnt):
        print("*", end=" ")
    print()

    if i < n-1:
        cnt -= 1
    
    else:
        cnt += 1