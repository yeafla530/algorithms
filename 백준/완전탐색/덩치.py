n = int(input())
data = [] # 입력받은 정보 저장할 리스트data
ans = [] # 등수정보 저장할 리스트 ans

for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    
    ans.append(count + 1)


for d in  ans:
    print(d, end=" ")