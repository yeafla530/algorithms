s = input()
arr = list(s)

second = arr[1]
first = arr[0]


for i in range(len(arr)):
    if arr[i] == second:
        arr[i] = first

print(''.join(arr))