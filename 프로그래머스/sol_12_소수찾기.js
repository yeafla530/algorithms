// 에라토스테네스의 체
function solution(n) {
    var answer = 0;
    let prime = [false, false, ...Array(n-1).fill(true)]
    console.log(prime)
    for (let i = 2; i *i <= n; i++) {
        if (prime[i]) {
            for (let j = i*2; j <= n; j+=i ) {
                prime[j] = false
            }           
        }
    }
    console.log(prime.filter(Boolean))
    return prime.filter(Boolean).length;
}


// 루트 사용
function isPrime(num) {
    for (let i = 2; i*i <= num; i++) {
        if (num % i === 0) {
            return false
        }
    }
    return true
}

function solution(n) {
    var answer = 0;
    for (let num = 2; num <= n; num += 1) {
        if (isPrime(num)) {
            answer += 1
        }
    }
    
    
    return answer
}