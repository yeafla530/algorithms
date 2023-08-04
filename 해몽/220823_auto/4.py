n = int(input())
words = []

for i in range(n):
    words.append([input(), i]) # (기존단어, index)


def get_common_prefix_len(i, j): # i번째 단어와 j번째 단어의 최대 공통 prefix 길이 계산
    print(i, j)
    if i < 0 or j < 0 or i >= n or j >= n: # 유효하지 않은 인덱스 무시하기
        return 0
    for k in range(0, 20):
        if words[i][0][k] != words[j][0][k]:
            return k 
    
    return -1



words.sort()
ans = ["" for _ in range(n)] # ans[i] = i번째 문자열의 압축결과

print(words)
for i in range(n):
    prev_len = get_common_prefix_len(i-1, i)
    next_len = get_common_prefix_len(i, i+1)
    print(prev_len, next_len)
    length = max(prev_len, next_len) + 1 # 압축하게 되는 길이
    print(length)
    ans[words[i][1]] = words[i][0][:length]


for i in range(n):
    print(ans[i])

# 7
# APPLEZZZZZZZZZZZZZZZ
# APPZZZZZZZZZZZZZZZZZ
# APPLKZZZZZZZZZZZZZZZ
# BANANAZZZZZZZZZZZZZZ
# BAKEZZZZZZZZZZZZZZZZ
# CALIFORNIAZZZZZZZZZZ
# CATZZZZZZZZZZZZZZZZZ

