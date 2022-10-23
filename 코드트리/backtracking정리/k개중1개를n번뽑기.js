let n = 3
let answer = []

function printAnswer() {
    for (const p in answer) {
        console.log(`${p}`)
    }
}

function choose(cnt) {
    if (cnt == n) {
        printAnswer()
        return 
    }

    for (let i = 0; i < 2; i++) {
        answer.push(i)
        choose(cnt+1)
        answer.pop()
    }
}



choose(0)