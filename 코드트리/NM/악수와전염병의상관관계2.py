# k번악수, P: 처음 전염
n, k, p, num = map(int, input().split())
situation = [tuple(map(int, input().split())) for _ in range(num)]
situation.sort(key=lambda x: x[0])
people = [0] * (n+1)
infected = [0] * (n+1)

infected[p] = True


for t, target1, target2 in situation:
    # if people[x] > 1:
    #     people[x] -= 1
    #     if people[y] == 0:
    #         people[y] = k+1
    #     else:
    #         people[y] -= 1

    # 감염되어있을 경우 악수 횟수 증가
    if infected[target1]:
        people[target1] += 1
    if infected[target2]:
        people[target2] += 1
    
    # target1이 감염되어있고, 아직 K번 이하로 악수했으면 target2 전염
    if people[target1] <= k and infected[target1]:
        infected[target2] = True
    # target2가 감염되어있고, 아직 K번 이하로 악수했으면 target1전염
    if people[target2] <= k and infected[target2]:
        infected[target1] = True

for i in range(1, n+1):
    if infected[i]:
        print('1', end="")
    else:
        print('0', end="")

    



