n = int(input())
arr1 = list(map(int, input().split()))


m = int(input())
arr2 = list(map(int, input().split()))

compare_num = set(arr1)

for elem in arr2:
    if elem not in compare_num:
        print(0, end=" ")
    else:
        print(1, end=" ")
