n, m = map(int, input().split())
arr = []

# 해설 풀이
# 몇개 들어있는지

def combination(curr_num, cnt):
    if curr_num == n+1:
        if cnt == m:
            print(*arr)
        return
    
    # 오름차순으로 출력하기 위해 순서도 중요
    arr.append(curr_num)
    combination(curr_num+1, cnt+1)
    arr.pop()

    # curr_num이 포함되지 않는 경우
    combination(curr_num+1, cnt)



combination(1, 0)