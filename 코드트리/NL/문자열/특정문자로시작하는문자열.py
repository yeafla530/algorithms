n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

word = input()
count = 0 
avg = 0
for elem in arr:
    if elem[0] == word:
        count += 1
        avg += len(elem)

print(f"{count} {avg / count:.2f}")

