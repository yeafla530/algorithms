// 내 풀이
function solution(n) {
    let answer = 0;
    let arr = [0, 1]
    let mino_one = 0
    let mino_two = 0
    for (let i = 2; i < n; i++) {
        mino_one = arr[i-1] % 1234567
        mino_two = arr[i-2] % 1234567
        

        arr.push(mino_one + mino_two)
    }
    
    return (arr[n-1] + arr[n-2]) % 1234567;
}

// DP
function solution(n) {
    let MAXINT = 100000
    let ans = 0
    let dp = new Array(MAXINT).fill(0)
    
    dp[1] = 1
    dp[2] = 1
    
    for (let i = 3; i <= n; i++) {
        dp[i] = (dp[i-1] + dp[i-2])%1234567
    }
    
    return dp[n]
    
}



// 다른 사람 풀이
function solution(n) {
    let a = 0, b = 1, f = 1;
    for (let i = 2; i <= n; i++) {
        f = (a + b) % 1234567
        a = b % 1234567
        b = f % 1234567
    }
    return f;
  }
  