def print_rectangle(n):
    cnt = 1

    for i in range(n):
        for j in range(n):
            print(cnt, end=" ")

            if cnt < 9:
                cnt += 1
            else:
                cnt = 1
        print()



n = int(input())

print_rectangle(n)