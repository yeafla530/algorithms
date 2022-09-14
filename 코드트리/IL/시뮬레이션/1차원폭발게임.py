n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

start_idx = 0
def get_end_idx(number, start):
    for end in range(start+1, len(numbers)):
        if numbers[end] != number:
            return end - 1
    return len(numbers) - 1

while True:
    did_boom = False

    for curr_idx, number in enumerate(numbers):
        if number == 0:
            continue
        
        end_idx = get_end_idx(number, curr_idx)
        

        if end_idx - curr_idx + 1 >= m:
            numbers[curr_idx:end_idx+1] = [0] * (end_idx - curr_idx)
            # print(numbers)
            did_boom = True
            curr_idx = end_idx+1
    
    numbers = list(filter(lambda x: x > 0, numbers))

    if not did_boom:
        break
    
print(len(numbers))
for number in numbers:
    print(number)


