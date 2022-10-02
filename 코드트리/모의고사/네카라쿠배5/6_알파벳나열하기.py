# 백트레킹으로만 풀면되는줄 알았는데 시초 걸림
# Backtracking + count array
# 각 문자마다 몇번씩 등장했는지 Count Array로 관리하면 중복없이 사전 순으로 만들 수 있다
# 시간 복잡도 O(min(N!, 10000))
MAX_PRINT_NUM = 10000

word = input()
freq = {}

print_num = 0


def find_permutation(new_word):
    global print_num

    # 최대 출력 횟수 넘으면 종료
    if print_num == MAX_PRINT_NUM:
        return
    
    # 선택이 끝났으면 종료조건
    if len(new_word) == len(word):
        print_num += 1
        print(new_word)
        return
    
    # 알파벳 다 둘러봄
    for i in range(26):
        c = chr(ord('a')+i)
        # 아직 해당 문자 사용할 수 있으면
        if freq.get(c, 0) > 0:
            freq[c] -= 1
            find_permutation(new_word+c)
            freq[c] += 1


# 지금까지 만들어진 문자열을 new_wort라 했을 때
# 탐색을 계속 진행
for c in word:
    freq[c] = freq.get(c, 0) + 1

find_permutation("")


