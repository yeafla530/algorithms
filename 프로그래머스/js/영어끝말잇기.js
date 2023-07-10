function solution(n, words) {
    var answer = [0, 0];
    
    for (let i = 0; i < words.length; i++) {
        let word = words[i]
        let p = i % n + 1
        let turn = Math.ceil((i+1)/n)
        console.log(p, turn)
        
        if (i > 0) {
            let last = words[i-1].split("").pop()
            // 중복이거나 이어지지 않으면
            if (i > words.indexOf(word) || words[i][0] !== last) {
                answer = [p, turn]
                break
            }
        }
    }
    

    return answer;
}