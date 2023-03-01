# 내 풀이
# g
# h
# g or h == 
# 최대 사진의 크기 찾는 프로그램

MAX_INT = 100
n = int(input())
arr = [0] * (MAX_INT+1)

for _ in range(n):
    idx, s = input().split()
    arr[int(idx)] = s 

max_count = 0
for i in range(0, MAX_INT+1):
    for j in range(i, MAX_INT+1):
        g = 0
        h = 0
        if arr[i] != 0 and arr[j] != 0:
            for k in range(i, j+1):
                if arr[k] == 'G':
                    g += 1
                elif arr[k] == 'H':
                    h += 1
            
            if g == 0 and h == j-i+1:
                max_count = max(max_count, j-i+1)
            elif h == 0 and g == j-i+1:
                max_count = max(max_count, j-i+1)
            elif g == h and g != 0 and h != 0:
                max_count = max(max_count, j-i+1)

print(max_count-1)




# 사진의 크기는 양쪽 끝에 있는 사람간의 거리
MAX_INT = 100
n = int(input())
arr = [0] * (MAX_INT + 1)
for _ in range(n):
    i, m = input().split()
    i = int(i)
    arr[i] = 1 if m == "G" else 2

# 최대사진크기 찾기
# G와 H개수가 같아지는
# 범위
max_photo = 0
for i in range(MAX_INT+1):
    # 개수 i+1부터 늘어남
    # i가 0일 때, j 는 0 ~ 100 까지 늘어날 수 있고
    for j in range(i+1, MAX_INT+1):
        # 양끝에 사람이 있는지 확인
        # print(i, j)
        # 맨앞 idx와 맨끝 idx 사람있는지 확인
        if arr[i] == 0 or arr[j] == 0:
            continue
        g = 0
        h = 0
        # k는 i부터 j까지의 구간 
        for k in range(i, j+1):
            if arr[k] == 1:
                g += 1
            elif arr[k] == 2:
                h += 1
        
        if g == 0 or h == 0 or g == h:
            leng = j - i
            max_photo = max(max_photo, leng)
print(max_photo)