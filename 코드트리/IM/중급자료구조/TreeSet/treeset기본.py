from sortedcontainers import SortedSet

n = int(input())
s = SortedSet()

for _ in range(n):
    arr = list(input().split())

    if arr[0] == "add":
        s.add(int(arr[1]))
    elif arr[0] == "remove":
        s.remove(int(arr[1]))
    elif arr[0] == "find":
        if int(arr[1]) in s:
            print("true")
        else:
            print("false")
    elif arr[0] == "lower_bound":
        idx = s.bisect_left(int(arr[1]))
        if idx < len(s):
            print(s[idx])
        else:
            print(None)
    elif arr[0] == "upper_bound":
        idx = s.bisect_right(int(arr[1]))
        if idx < len(s):
            print(s[idx])
        else:
            print(None)
    elif arr[0] == "largest":
        if s:
            print(s[-1])
        else:
            print(None)

    elif arr[0] == "smallest":
        if s:
            print(s[0])
        else:
            print(None)
