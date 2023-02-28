n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
box = 3
max_count = 0
ans = 0

x1, y1 = 0, 0
x2, y2 = 0, 0

for i in range(n):
    for j in range(n-2):
        count = 0
        for z in range(3):
            if arr[i][j+z]:
                count += 1

        if max_count <= count:
            max_count = max(max_count, count)
            x1 = i
            y1= j

for i in range(3):
    visited[x1][y1+i] = 1
ans = max_count

max_count = 0
for i in range(n):
    for j in range(n-2):
        count = 0
        if visited[i][j+z]:
            break
        for z in range(3):
            if arr[i][j+z]:
                count += 1

        if max_count < count:
            max_count = max(max_count, count)

ans += max_count


print(ans)
            

        
# 답지
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0
# Step1
# 첫번째 격자를 놓는다
for i in range(n):
    # 격자를 벗어나지 않을 범위로만 잡는다
    for j in range(n-2):
        # 두번째 격자를 놓는다 (k, l)
        for k in range(n):
            # 격자를 벗어나지 않을 범위로만 잡는다
            for l in range(n-2):
                # Step2. 두 격자가 겹치는 경우에는 가짓수로 세지 않는다
                if i == k and abs(j - l) <= 2:
                    continue
                
                cnt1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                cnt2 = arr[k][l] + arr[k][l+1] + arr[k][l+2]
                max_cnt = max(max_cnt, cnt1+cnt2)

print(max_cnt)