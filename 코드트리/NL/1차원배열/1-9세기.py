n = int(input())
arr = [0 for _ in range(10)]


nums = list(map(int, input().split()))

for elem in nums:
    arr[elem] += 1


for i in range(1, 10):  
    print(arr[i])