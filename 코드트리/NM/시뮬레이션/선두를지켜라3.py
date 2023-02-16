MAX_NUM = 1000000
n, m = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]
b = [tuple(map(int, input().split())) for _ in range(m)]

a_dis = [0 for _ in range(MAX_NUM)]
b_dis = [0 for _ in range(MAX_NUM)]

time_a = 1
for v, t in a:
    for tm in range(time_a, t+time_a):
        a_dis[tm] = a_dis[tm-1] + v
    time_a += t


time_b = 1
for v, t in b:
    for tm in range(time_b, t+time_b):
        b_dis[tm] = b_dis[tm-1] + v
    time_b += t

# print(a_dis) # 0, 1, 2, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27
# print(b_dis) # 0, 2, 4, 6, 7, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35

count = 0
leader = 0

for i in range(1, MAX_NUM):
    if a_dis[i] > b_dis[i] and leader != 1:
        leader = 1
        count += 1

    elif a_dis[i] < b_dis[i] and leader != 2:
        leader = 2
        count += 1

    elif a_dis[i] == b_dis[i] and leader != 3:
        leader = 3
        count += 1

print(count-1)        



    

