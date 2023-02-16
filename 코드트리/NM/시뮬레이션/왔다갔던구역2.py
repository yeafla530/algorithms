# 내풀이
n = int(input())
# 2번 이상 지나간 영역의 크기 출력
arr = [0] * 2001
start = 1000
for _ in range(n):
    a, b = input().split()
    a = int(a)

    if b == "R":
        for _ in range(a):
            arr[start] += 1
            start += 1

    else:
        for _ in range(a):
            start -= 1
            arr[start] += 1


ans = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        ans += 1

print(ans)



# 답지
n = int(input())
segment = []
start = 1000
for _ in range(n):
    distance, direct = input().split()
    distance = int(distance)


    if direct == 'R':
        segment.append([start, start+distance])
        start = start + distance
    else:
        segment.append([start-distance, start])
        start = start - distance
# print(segment)
check = [0] * 2000
for s, e in segment:
    for i in range(s, e):
        check[i] += 1
        

result = 0
for i in range(2000):
    if check[i] >= 2:
        result += 1
print(result)
    
    
