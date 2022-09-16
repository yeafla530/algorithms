# 나는 서로 반대의 값을 갖는 dict를 2개 작성하여 풀이했다
# 해설에서는 ord를 사용하여 풀이함
n, m = map(int, input().split())
d = {}
num = {}

for i in range(n):
    key = input()
    d[key] = i+1
    num[i+1] = key 

# print

for i in range(m):
    v = input()

    if v in d:
        print(d[v])
    
    else:
        print(num[int(v)])



n, m = map(int, input().split())
words = [input() for _ in range(n)]

string_to_num = dict()

for i in range(n):
    string_to_num[words[i]] = i + 1

for _ in range(m):
    word = input()

    # 입력된 값이 숫자일 때 > 나는 key값이 존재하지 않을때로 가정
    if ord('0') <= ord(word[0]) <= ord('9'):
        num = int(word)
        print(words[num - 1])
    
    else:
        print(string_to_num[word])
    
