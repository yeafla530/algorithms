n = int(input())
tail = [0] * 200001
start = 100000
for _ in range(n):
    num, p = input().split()
    num = int(num)

    if p == "L":
        tail[start] = 1
        for _ in range(num-1):
            start += 1
            tail[start] = 1

    else:
        tail[start] = 2
        for _ in range(num-1):
            start -= 1
            tail[start] = 2

print(tail.count(1), tail.count(2))