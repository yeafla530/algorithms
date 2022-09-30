# 이 문제는 굳이 시간을 h, m 따로 보지 않고 분으로만 판단하면됨
h, m = input().split(':')
x = int(input())
k = int(input())

minute = int(h) * 60 + int(m)
s = set()
ans = 0


def check(minute):
    h = minute // 60
    m = minute % 60

    sum_v = h // 10 + h % 10 + m // 10 + m % 10

    if sum_v == k:
        return True
    
    return False



while True:
    if minute in s:
        break
    
    if check(minute):
        ans += 1

        
    s.add(minute)
    minute += x
    minute = minute % 1440
    # print(minute)

print(ans)
