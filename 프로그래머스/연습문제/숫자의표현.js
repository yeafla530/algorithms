// 효율성 통과 못함
function solution(n) {
    let num = n
    let idx = 0
    let count = 1
    for (let i = 1; i < Math.ceil(n/2); i++) {
        while (num > 0) {
            num -= i + idx
            idx += 1
        }
        if (num === 0) {
            count += 1
        } 
        num = n
        idx = 0
    }
    return count;
}

// n의 홀수 약수 개수 = 연속되는 합으로 n을 표현할 수 있는 개수
function solution(n) {
    let answer = 0
    for (let i = 1; i <= n; i++) {
        if (n % i === 0 && i % 2 === 1) {
            answer ++
        }
    }
    return answer;
}