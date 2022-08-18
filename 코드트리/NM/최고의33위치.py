n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def get_max_coin(i, j):
    c = 0
    for x in range(i, i+3):
        for y in range(j, j+3):
            if arr[x][y] == 1:
                c += 1

    return c   

max_coin = 0
for i in range(n-3+1):
    for j in range(n-3+1):
        coin = get_max_coin(i, j)
        max_coin = max(max_coin, coin)


print(max_coin)


# 강사님 풀이
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 기준점 n-2, n-2 
# 9 * (n-2) * (n-2) => n 의 max값은 20 = 3600 < 1억
max_gold = 0
# (row, col) 3*3 정사각형 기준점
for row in range(n-2):
    for col in range(n-2):

        # 3*3 정사각형 gold 합
        num_of_gold = 0
        for i in range(row, row+3):
            # for j in range(col, col+3):
                # 좀더 간단하게 각행에 대해 sum 합 구함
                num_of_gold += sum(arr[i][col:col+3])
        # 결과값 업데이트
        max_gold = max(max_gold, num_of_gold)

print(max_gold)


# 재미로 보는 코드
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_gold = 0
# (row, col) 3*3 정사각형 기준점
for row in range(n-2):
    for col in range(n-2):

        # 3*3 정사각형 gold 합
        num_of_gold = sum([sum(arr[r][col : col+3]) for r in range(row, row+3) ]) 
        
        # 결과값 업데이트
        max_gold = max(max_gold, num_of_gold)

print(max_gold)