function solution(begin, target, words) {
    let answer = 0
    let visited = Array(word.length).fill(false)
    let q = []
    if (!(words.includes(target))) {
        return 0
    }

    q.push(begin)


    while (q.length) {
        for (let a = 0; a < q.length; a++) {
            let change = q.shift()
            if (change == target) {
                return answer
            }

            for (let i = 0; i < words.length; i++) {
                let change = 0
                for (let j = 0; j < target.length; j++) {
                    if (change[j] === words[i][j]) {
                        check += 1
                    }
                }

                if ((check === target.length-1) && (visited[i]) === false) {
                    visited[i] = true
                    q.push(words[i])
                }

                if (q.includes(target)) {
                    break
                }
            }
        }
        answer += 1
    }



}


graph = Array.from(Array(row), () => Array(column).fill(-1))