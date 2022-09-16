n = int(input())
d = {}
# 순서 상관없이 같은 단어들이 같은 횟수로 포함되어있는 문자들 찾기
# print(lst)
for _ in range(n):
    st = input()
    st = sorted(st)

    string = ""
    for s in st:
        string += s
    d[string] = d.get(string, 0) + 1
    
result = 0
for key, value in d.items():
    result = max(result, value)

print(result)
    
