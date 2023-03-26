n, m = map(int, input().split())  # 보석종류, 무게
firstDp = [0 for _ in range(10001)]
endDp = [0 for _ in range(10001)]
array = [0]

for _ in range(n):
    w, v = map(int, input().split())
    # if w <= m:
    firstDp[w] += v
    endDp[w] += v
    array.append((w, v))  # 무게, 가치

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if array[j][0] <= i:
            if i - array[j][0] != array[j][0]:
                endDp[i] = max(endDp[i], firstDp[array[j][0]] + firstDp[i - array[j][0]])
            else:
                endDp[i] = max(endDp[i], firstDp[array[j][0]])

print(max(endDp))