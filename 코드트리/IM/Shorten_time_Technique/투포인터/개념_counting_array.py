# 특정 구간을 잘 골라 구간 내 같은 숫자가 3개이상 있지않은 경우 중
# 가장 큰 구간의 크기를 구하는 프로그램

# 시작점 i에 대해 어디까지 진행해도 되는지 빠르게 판단할 수 있다면 Two Pointer방법으로 풀린다

# Counting Array기법
# 각 숫자마다 몇번씩 나왔는지 counting해주는 배열 추가적으로 만들어 관리
# 현재 [i, j]구간 내 각 숫자가 몇개씩 들어있는지 계속 트래킹 가능
# j를 더 증가시키기전 현재 Aj+1이 더 추가되면 같은 숫자가 3개가 되지는 않는지 O(1)로 즉각적으로 확인가능

arr = [0, 2, 1, 2, 2, 1, 3, 1]
count_array = [0] * 4
n = 7

# 가능한 구간중 최대 크기
ans = 0

# 구간잡기
j = 0

for i in range(1, n+1):
    while j + 1 <= n and count_array[arr[j+1]] != 2:
        count_array[arr[j+1]] += 1
        j += 1
    
    ans = max(max, j - i + 1)

    count_array[arr[i]] -= 1

print(ans)
