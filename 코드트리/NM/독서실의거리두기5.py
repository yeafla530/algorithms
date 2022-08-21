n = int(input())
arr = list(map(int, list(str(input()))))

def min_dist():
    dist = n
    # 둘 다 1인 곳에 대해
    # 모든 쌍을 조사하여, 그 중 가장 가까운 거리를 구합니다.
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == 1 and arr[j] == 1:
                dist = min(dist, j-i)
    
    return dist



max_cnt = 0
# 들어갈 위치를 일일이 정해보며
# 그 상황에서 가장 가까운 사람간의 거리를 구해
# 가능한 경우 중 최댓값을 계산합니다.
for i in range(n):
    if arr[i] == 0:
        arr[i] = 1
        max_cnt = max(max_cnt, min_dist())
        arr[i] = 0

print(max_cnt)