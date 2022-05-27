// 최대한 많은 부서의 물품을 구매해 줄 수 있도록 
// 각 부서가 신청한 금액만큼을 모두 지원해줘야함
// 신청금액 d, 예산 budget
// 최대 몇 개의 부서에 물품을 지원
// 남은 2원으로 나머지 부서를 지원해 주지 않습니다


// 부분합문제? no 
function solution(d, budget) {
    var answer = 0;
    d = d.sort((a,b) => a - b)
    sum = 0
    for (let i = 0; i < d.length; i++) {
        sum += d[i]
        answer += 1
        if (sum > budget){
            // console.log(budget, d[i])
            return answer - 1
        }
    }
    return answer;
}