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
        // 에라토스테네스의 체에 의해 
        // 제곱근 이하의 수만으로 소수 판별 가능
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
        // 첫번째 index가 끝까지 도달하면 answer return
        if (first === end - 2) {
            return answer
          // 그 외
        } else {
            // second가 도달할 수 있는곳까지 도달했을 때
            if (second === end - 1) {
                first += 1
                second = first + 1
                third = second + 1
              // 그 외
            } else {
                // third가 끝까지 도달했을 때
                if (third === end) {
                    second += 1
                    third = second + 1
                // 그 외
                } else {
                    third += 1
                }
            }
        }
        
        
    }
}