# 이어 붙였을 때 길이가m이 되는 문자열 중 사전순으로 가장 앞선 문자열
n, m = map(int, input().split())
arr = list(input().split())
visited = [0] * (n)
ans = ""
# 지금까지 뽑힌 문자열을 순서대로 이어붙힌 문자열을 curr_str로 저장하여 다음에 뽑을 문자열 선택

def choose(cur_txt):
    global ans
    # 이미 m개를 넘어버렸으면 return
    if len(cur_txt) > m:
        return
    
    if len(cur_txt) == m:
        if ans == "" or ans > cur_txt:
            ans = cur_txt
        return
    
    # 1. n개의 문자열에 대해 이미 사용됐는지 여부 확인
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            choose(cur_txt+arr[i])
            visited[i] = False

    

choose("")
if ans == "":
    print(-1)
else:
    print(ans)