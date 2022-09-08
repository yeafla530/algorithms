n = int(input())
a = [0] + list(map(int, input().split()))
store = []
result = []

result.append(0)
store.append(1)
# 송전탑 확인
for i in range(2, n+1):
    unblock = []
    # 저장된 index값
    for j in range(len(store)-1, -1, -1):
        # 현재 송전탑보다 비교한 송전탑이 더 큰 경우
        s = store[j]
        if a[s] >= a[i]:
            # 부딪히는 송전탑
            result.append(s)
            # 비교할 송전탑에 현재 index넣기
            store.append(i)
            break
        # 부딪히지 않을 경우
        else:
            # 끝까지 확인했을 때
            if j == 0:
                result.append(0)
            # 부딪히지 않은 store[j] 송전탑
            unblock.append(j)

    # result에 들어간 index까지만 저장 
    for u in unblock:
        store.pop(u)
    store.append(i)

print(*result)