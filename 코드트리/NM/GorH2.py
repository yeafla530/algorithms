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