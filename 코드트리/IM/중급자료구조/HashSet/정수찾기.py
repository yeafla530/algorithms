n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

set_arr = set(arr1)

for elem in arr2:
    if elem in set_arr:
        print(1)
    else:
        print(0) 