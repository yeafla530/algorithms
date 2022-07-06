function solution(participant, completion) {
    // 둘 다 정렬
    participant.sort()
    completion.sort()
    // console.log(participant, completion)
    for (let i =0; i < completion.length; i++) {
        if (participant[i] !== completion[i]) {
            return participant[i]
        }
    }
    return participant[participant.length - 1]
}