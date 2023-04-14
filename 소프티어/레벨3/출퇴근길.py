import sys
sys.setrecursionlimit(10**6)

# s => T로 가는 출근경로와 T => S로 가는 퇴근길 경로에 모두 포함될 수 있는 정점의 개수세기
# 출퇴근길에서 목적지 정점 방문하고 나면 움직이지 ㅇ나흔다
# S, T는 마지막에 정확히 한번만 등장

n, m = map(int, input().split())
# 정점의 개수 + 1만큼 초기화
# 이유 : 정점의 번호를 0번부터 n-1번까지 쓸수 있어서 달라짐
arr = [[] for _ in range(n+1)]
adj_r = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    adj_r[y].append(x)
s, t = map(int, input().split())
# print(arr) # 해당 idx에 있는 노드로 가는길
# print(adj_r) # 해당 숫자에서 해당 idx 노드로 오는길
# 간선의 방향을 다 바꿔놓은 것 추가하기

# 방문할 노드, 
def dfs(now, adj, visit):
    # 방문한 곳이면
    if visit[now] == 1:
        return
    
    visit[now] = 1
    for neighbor in adj[now]:
        dfs(neighbor, adj, visit)
        
    return

# 출근길
fromS = [0]*(n+1)
fromS[t] = 1
dfs(s, arr, fromS)

# 퇴근길
fromT = [0]*(n+1)
fromT[s] = 1
dfs(t, arr, fromT)

toS = [0]*(n+1)
dfs(s, adj_r, toS)

toT = [0]*(n+1)
dfs(t, adj_r, toT)

count = 0
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        count+=1

print(count-2)