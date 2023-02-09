a = input()
arr = list(input())

for i in range(len(arr)):
    if arr[i] == 'L':
        a = a[1:] + a[0]
    else:
        a = a[-1] + a[:-1]

print(a)