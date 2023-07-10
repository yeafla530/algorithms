function solution(people, limit) {
    let answer = 0;
    let left = 0
    let right = people.length - 1
    people.sort((a, b) => b - a)
    console.log(people)
    
    while (left < right) {
        if (people[right] + people[left] <= limit) {
            right -= 1
            left += 1
        } else {
            left += 1
        }
        answer += 1
    }
    if (left == right) answer ++
    return answer;
}