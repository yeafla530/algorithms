function solution(participant, completion) {
    // 1~10만
    // 1. participant에 담긴 array를 map으로 옮긴다
    let map1 = new Map()
    result = ""    
    for (part of participant) {
        if (map1.has(part)) {
            map1.set(part, map1.get(part)+1)
        } else {
            map1.set(part, 1)
        }
    }

    for (p of completion) {
        map1.set(p, map1.get(p)-1)
    }
    
    for (let key of map1.keys()) {
        if (map1.get(key) == 1) {
            result = key
        } 
    }
    
    return result
}


function solution(participant, completion) {
    var people = new Map()
    for (let i = 0; i < participant.length; i++) {
        if (people.has(participant[i])) {
            num = people.get(participant[i]) + 1
            people.set(participant[i], num)
        } else {
            people.set(participant[i], 1)
        }
    }
    for (let j = 0; j < completion.length; j++) {
        num = people.get(completion[j]) - 1
        people.set(completion[j], num)
    }
    
    
    for ([key, value] of people) {
        if (value === 1) {
            return key
        }
    }
    
    
}