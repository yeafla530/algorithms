# 부분수열 판별문제
# [5, 1, 5, 3, 1, 4]일때 [5, 1, 4]라면 순서대로 존재하므로 부분수열이다

# 수열 B의 원소들은 가능하면 수열 A의 가장 앞에 있는 원소와 매칭하는것이 항당 이득

# i, j가 서로 다른 수열을 가리키고 있는 투포인트

A = [0, 5, 1, 5, 3, 1, 4]
B = [0, 5, 1, 4]
n, m = 6, 3

def is_subsequence():
    i = 1

    #B원소 기준 순서대로 매칭 가능한지 확인
    for j in range(1, m+1):
        while i <= n and A[i] != B[j]:
            i += 1
        
        if i == n+1:
            return False
        
        else:
            i += 1

    return True


if is_subsequence():
    print("Yes")
else:
    print("No")