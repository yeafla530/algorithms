n, m = map(int, input().split())
load1 = [0] * (101)
load2 = [0] * (101)

start = 0
for _ in range(n):
    end, ver = map(int, input().split())

    for i in range(start+1, start+end+1):
        load1[i] = ver
    
    start += end

start = 0
for _ in range(m):
    end, ver = map(int, input().split())

    for i in range(start+1, start+end+1):
        load2[i] = ver
    
    start += end




ans = 0
for i in range(101):
    ans = max(ans, load2[i]-load1[i])


print(ans)