# 원소의 수, 질의의 수
n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        print(arr[nums[1]-1])
    elif nums[0] == 2:
        if nums[1] in arr :
            print(arr.index(nums[1]) + 1)
        else:
            print(0)
    else:
        print(*arr[nums[1]-1:nums[2]])