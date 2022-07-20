// 제일 오래걸린 시간 : 3.7ms
function solution(nums) {
    var answer = 0;
    let first = 0;
    let second = 1;
    let third = 2;
    let end = nums.length - 1
    
    while (true) {
        // 합계
        let sum = nums[first] + nums[second] + nums[third]
        let isPrime = true
        // console.log(sum)
        for (let i = 2; i*i <= sum; i++) {
            // 소수가 아님
            if (sum % i === 0) {
                isPrime = false
                // console.log(sum, i)
                break
            }
        }
        // 소수면 + 1
        if (isPrime) {
            answer += 1
        }
        
        // 수 증가시키기
        // 첫번째 index가 
        if (first === end - 2) {
            return answer
        } else {
            if (second === end - 1) {
                first += 1
                second = first + 1
                third = second + 1
            } else {
                if (third === end) {
                    second += 1
                    third = second + 1
                } else {
                    third += 1
                }
            }
        }
        
        
    }
}