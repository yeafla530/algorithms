# 변수 선언 및 입력:
num_str = input()

# 처음에 0인 부분은 출력하지 않도록 합니다. 
can_print = False

# 문자열을 거꾸로 순회합니다.
for digit in num_str[::-1]:
	if digit != '0':
		can_print = True
	
	if can_print:
		print(digit, end="")