import sys
t = int(input())
# 각 자리의 전구를 2차 배열로 표현

number = [[0]*7 for _ in range(10)]

number[0] = [1, 1, 1, 0, 1, 1, 1]
number[1] = [0, 0, 1, 0, 0, 1, 0]
number[2] = [1, 0, 1, 1, 1, 0, 1]
number[3] = [1, 0, 1, 1, 0, 1, 1]
number[4] = [0, 1, 1, 1, 0, 1, 0]
number[5] = [1, 1, 0, 1, 0, 1, 1]
number[6] = [1, 1, 0, 1, 1, 1, 1]
number[7] = [1, 1, 1, 0, 0, 1, 0]
number[8] = [1, 1, 1, 1, 1, 1, 1]
number[9] = [1, 1, 1, 1, 0, 1, 1]

n = 5
for _ in range(t):
    count = 0
    arr = [[0]*7 for _ in range(5)]
    arr2 = [[0]*7 for _ in range(5)]
    a, b = input().split()
    a = list(a)
    b = list(b)

    start = n-len(a)
    for i in range(start, 5):
        # i : 1, 2, 3, 4
        # sn : 0, 1, 2, 3
        sn = i-start

        num = int(a[sn])
        arr[i] = number[num]


    s2 = n - len(b)
    for j in range(s2, 5): # 111
        sn2 = j - s2
        
        num = int(b[sn2])
        arr2[j] = number[num]
        


    for i in range(5):
        for j in range(7):
            if arr[i][j] != arr2[i][j]:
                count += 1 
    
    print(count)


    