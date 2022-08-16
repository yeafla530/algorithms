# 점프를 통해서 이동가능, 점프 진행시 항상 현재위치에 적혀있는 색, 점프한 후 칸에 적혀잇는 색이 달라야함 
# 현재 위치에서 적어도 한칸이상 오른족에 있는 위치, 동시에 현재위치에서 적어도 한칸이상 아래쪽에 있는 위치로 점프가능
# 시작 도착지점 제외하고 점프하며 도달한 위치가 정확히 2곳뿐이어야함

r, c = map(int, input().split())
mapping = [list(input().split()) for _ in range(r)]
cnt = 0
# 점프후첫번째로 밟게되는위치, 두번째로 밟게되는 위치를 전부정해보는 완탐진행
for i in range(1, r):
    for j in range(1, c):
        for k in range(i+1, r-1):
            for l in range(j+1, c-1):
                if mapping[0][0] != mapping[i][j] and\
                    mapping[i][j] != mapping[k][l] and\
                    mapping[k][l] != mapping[r-1][m-1]:
                        cnt += 1
print(cnt)