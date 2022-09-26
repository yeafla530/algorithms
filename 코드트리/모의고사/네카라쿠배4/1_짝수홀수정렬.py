# 짝수는 오름차순
# 홀수는 내림차순

n = int(input())
arr = list(map(int, input().split()))

odds = []
evens = []

for i in arr:
    if i % 2:
        odds.append(i)
    
    else:
        evens.append(i)

evens.sort()
odds.sort(reverse=True)

for even, odd in zip(evens, odds):
    e = even
    o = odd
    print(e, o, end=" ")