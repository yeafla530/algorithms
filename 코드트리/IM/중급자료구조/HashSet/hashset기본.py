n = int(input())
s = set()

for _ in range(n):
    string, num = input().split()
    num = int(num)

    if string == 'add':
        s.add(num)

    elif string == 'remove':
        s.remove(num)
    else:
        if num in s:
            print('true')
        else:
            print('false')
        