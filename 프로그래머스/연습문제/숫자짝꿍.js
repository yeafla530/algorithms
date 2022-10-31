function solution(X, Y) {
    var answer = '';
    const n = Array.from(Array(10).fill(0))
    const twin = []
    
    for (let i = 0; i < X.length; i++) {
        n[X[i]] += 1
    }
    
    for (let j = 0; j < Y.length; j++) {
        if(n[Y[j]] > 0) {
            twin.push(Y[j])
            n[Y[j]] -= 1
        }
    }
    answer = twin.length > 0 ? twin.sort((a, b) => b - a).join("") : '-1'
    // console.log(answer)
    if (answer === '') answer = '-1'
    else if (Number(answer) === 0) answer = '0'
    
    return answer
}