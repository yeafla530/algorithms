import sys

si = sys.stdin.readline
R = int(si())
# 기록 받기
records = [si().split() for _ in range(R)]

# 등장하는 사람들에 대한 정렬
names = set([record[1] for record in records]) # set of the names

ans = 0 # 틀린 사람 수 기록 변수 
for name in names: # target person's name
    # 1. collect the records for the person
    # 한 사람에 대한 정보 
    rec = [record for record in records if record[1] == name]

    # 2. sort by the time
    rec.sort(key = lambda x: x[0])

    # 3. iterate & check the validity
    flag = True
    for i in range(len(rec)):
        # 짝수인데 out이면
        if i % 2 == 0 and rec[i][2] == "out":
            flag = False
        # 홀수인데 in이면
        elif i % 2 == 1 and rec[i][2] == "in":
            flag = False
    
    if not flag: # invalid case detected!
        ans += 1

print(ans)