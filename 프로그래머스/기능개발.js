function solution(progresses, speeds) {
    let answer = [0];
    let days = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index]))
    console.log(days)
    let maxDay = days[0];

    for (let i = 0, j = 0; i < days.length; i++) {
        if (days[i] <= maxDay) {
            console.log('1.',maxDay, answer)
            answer[j] += 1
        }  else {
            maxDay = days[i]
            console.log('2.',maxDay, answer)
            // j를 먼저 증가시켜야 그 전 값이 1로 
            //초기화 되지 않음
            answer[++j] = 1
            console.log('answer',answer)

        }
    }
    return answer
}