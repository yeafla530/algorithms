# 수열에 있는 수들을 합한 값을 구한다
# i가 소수인 Ai추출해서 더해준다

n = int(input())
arr = list(map(int, input().split()))

result = 0

def is_decimal(n):
	for i in range(2, int(n**(1/2))+1):
		if n % i == 0:
			return False
	
	return True


for i in range(1, n):
	if is_decimal(i+1):
		result += arr[i]
	

print(result)
		
		
		
