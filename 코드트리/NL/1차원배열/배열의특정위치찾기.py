arr = list(map(int, input().split()))

sum1 = sum(arr[1::2])
avg_list = arr[2::3]
avg = round(sum(avg_list) / len(avg_list), 1)

print(sum1, avg)