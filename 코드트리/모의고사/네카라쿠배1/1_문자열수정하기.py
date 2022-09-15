# 디버깅을 확인하기 위해 낸 문제
# TC를 직접 만들어서 확인해야하는 문제
st = list(input())

second = st[1]
fifth = st[4]

for i, s in enumerate(st):
    if s == second:
        st[i] = fifth

print(*st, sep="") 