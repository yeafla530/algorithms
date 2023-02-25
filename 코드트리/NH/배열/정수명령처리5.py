n = int(input())
lst = []
for _ in range(n):
    arr = list(input().split())
    if arr[0] == "push_back":
        lst.append(int(arr[1]))
    elif arr[0] == "get":
        arr[1] = int(arr[1])
        print(lst[arr[1]-1])
    elif arr[0] == "size":
        print(len(lst))
    elif arr[0] == "pop_back":
        lst.pop()
