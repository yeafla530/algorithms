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
    
    
