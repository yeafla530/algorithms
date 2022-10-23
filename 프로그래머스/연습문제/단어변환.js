var answer = 0;
let visited = Array(words.length).fill(false)
let queue = []
if (!(words.includes(target))) {
    return 0
}
else {
    queue.push(begin)
    while (queue.length !== 0) {
        // console.log('q', queue)
        // console.log(change[0])
        for (let a = 0; a < queue.length; a ++) {
            let change = queue.shift()
            if (change === target) {
                return answer
            }
            for (let i = 0; i < words.length; i++) {
                let check = 0
                // console.log(i)
                for (let j = 0; j < target.length; j++) {
                    // console.log(change[j], words[i][j])
                    if (change[j] === words[i][j]) {
                        check += 1
                    }
                }
                // console.log(check)
                if ((check === target.length-1) && (visited[i] === false)) {
                    // console.log('push', words[i])
                    visited[i] = true
                    queue.push(words[i])

                }
                if (queue.includes(target)) {
                    break
                }
            }
        }
        answer += 1
    }
}