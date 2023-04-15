
m, n, k = map(int, input().split())
# 식권 받을 수 있으면 secret 그렇지 않으면 nomal
# 메뉴 조작법
menu = list(map(int, input().split()))
push = list(map(int, input().split()))

ans = "normal"


for start in range(len(push)):
    if push[start] == menu[0]:
        is_secret = True
        for x in range(len(menu)):
            if start+x >= len(push):
                is_secret = False
                break
            if push[start+x] != menu[x]:
                is_secret = False
                break
        if is_secret:
            ans = "secret"
            break

print(ans)