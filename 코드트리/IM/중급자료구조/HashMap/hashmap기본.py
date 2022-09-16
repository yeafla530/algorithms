n = int(input())
a = [tuple(input().split()) for _ in range(n)]

d = {}

# print(a)
for i in range(n):
    command = a[i][0]
    k = int(a[i][1])

    if command == "add":
        d[k] = int(a[i][2]) 
    elif command == "remove":
        d.pop(k)
    else:
        # print(k, d)
        if k in d:
            print(d[k])
        else:
            print(None)



