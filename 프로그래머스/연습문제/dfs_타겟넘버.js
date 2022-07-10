// solution([1, 1, 1], 1)

function solution(numbers , target) {
    let answer = 0
    function subset(cnt, sum) {
        if (cnt === numbers.length) {
            if (sum === target) {
                answer += 1
            }
            return
        }
        subset(cnt+1, sum+numbers[cnt])
        subset(cnt+1, sum-numbers[cnt])
        
    }   
    subset(0, 0)
    return answer;
}