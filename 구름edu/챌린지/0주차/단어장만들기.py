import sys
input = sys.stdin.readline
word = list()
n, k = map(int, input().split())
for i in range(n):
    word.append(input().rstrip())
word.sort()
word.sort(key = lambda x : len(x))
print(word[k-1])