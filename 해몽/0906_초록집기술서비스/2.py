n = int(input())
alphabets = input().split()

# 중복제거를 위해
res = set() # 만들 수 있는 문자열들을 기록하는 배열
visited = [0 for _ in range(n)] # 각 알파벳 사용 여부

# 재귀
def func(str): #str: 지금까지 만들어진 문자열
    if len(str) == n:
        res.add(str)
        return

    for i in range(n):
        if visited[i]: continue
        # 마지막 문자열과 현재 선택한 문자가 똑같다면 추가하지 않음
        if len(str) > 0 and str[-1] == alphabets[i]: 
            continue
        
        visited[i] = 1
        func(str + alphabets[i])
        visited[i] = 0


func('')

res = sorted(list(res))

for x in res:
    print(x)