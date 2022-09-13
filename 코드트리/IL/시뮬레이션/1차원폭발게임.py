n, m = map(int, input().split())
bomb = [int(input()) for _ in range(n)]
box = []
is_posibble = False

# 더이상 폭탄이 터지지 않을때까지 반복
while True:
    # 모든 폭탄 번호가 같은 경우에는?
    temp = bomb[0]
    s, e = 0, 0
    cnt = 1
    for i in range(1, len(bomb)):
        print(bomb[i], temp)
        # 이전 번호와 현재 번호가 같은 경우
        if temp == bomb[i]:
            cnt += 1
        # end point + 1 
        # 개수 + 1

        # 이전 번호와 현재 번호가 다른 경우 
        else:
            e = i
            # 개수가 m보다 크거나 같은 경우 => 
            if cnt >= m:
                # print(cnt, m)
                # s부터 e까지 boom
                for j in range(s, e):
                    bomb[j] = 0
                # s, e, n 초기화
            s = i
            cnt = 1
            temp = bomb[i]
            # 개수가 m보다 작은경우 => 유지
    # print(bomb)
    e = len(bomb)
    # 마지막에 boom check (s, e까지)
    if cnt >= m:
        for j in range(s, e):
            bomb[j] = 0
    
    for i in range(len(bomb)):
        if bomb[i]:
            box.append(bomb[i])
    
    
    bomb = box[:]


    # 더이상 폭탄이 터질 수 없으면 break
    for i in range(len(bomb)-m+1):
        # 더이상 폭탄이 터질수 없는지 확인 
        if bomb[i:i+m].count(bomb[i]) >= m:
            is_posibble = True

    if not is_posibble:
        break

print(len(bomb))
if len(bomb):
    for i in range(len(bomb)):
        print(bomb[i])