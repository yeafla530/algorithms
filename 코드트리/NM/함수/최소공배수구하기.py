def find(a, b):
    min_num = min(a, b)
    s = 2
    ans = 1
    while min_num >= s:
        if a % s == 0 and b % s == 0:
            # print('True')
            a //= s
            b //= s
            min_num = min(a, b)
            ans *= s
            s = 2
        else:
            s += 1

    return ans * a * b



a, b = map(int, input().split())
print(find(a, b))
