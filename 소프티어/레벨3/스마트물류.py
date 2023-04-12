# 로봇들 위치에서 거리가 K이하인 부품만 잡을 수 있다
# 라인의 길이 N, 부품 거리 K, 
# 로봇과 부품의 위치가 주어졌을 때 부품을 집을 수 있는 로봇의 최대 수

n, k = map(int, input().split())
arr = list(input().split())

# 왼 오
dirs = [-1, 1]
visited = [0] * n

cnt = 0
# P : 로봇, H : 부품
for i in range(n):
    if arr[i] == "P":
        # 부품 탐색
        for j in range(i-k, i+k+1):
            if j < 0 or j > n:
                continue
                
            if r[j] == "H":
                cnt += 1
                r[j] == "A"
                break

print(cnt)
    