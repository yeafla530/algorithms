# 설치 위치로부터 거리 m이내에 있느 사람들까지만 사용가능
# 사람이 살고있는 곳이 아니더라도 설치 가능하지만
# 정수위치에만 설치가 가능 
# 모든 사람들이 사용할 수 있도록 필요한 최소의 와이파이수 출력

n, m = map(int, input().split())
arr = list(map(int, input().split()))

l = 2 * m + 1
cnt = 0
s = 0
while s < n:
    # 사람이 없으면 
    if not arr[s]:
        s += 1
        continue
    
    cnt += 1
    s += l

print(cnt)
        


