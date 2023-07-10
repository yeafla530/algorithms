function solution(numbers) {
    const temp = []
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            temp.push(numbers[i] + numbers[j])
        }
    }

    const answer = [...new Set(temp)]

    return answer.sort((a, b) => a - b)
}


// 순열을 이용한 풀이
function combinations(arr, n) {
    if (n === 1) return arr.map((v) => [v]);
    
    
    let result = []
    let sum = 0
    arr.forEach((fixed, idx, arr) => {
        const rest = arr.slice(idx + 1)
        const combis = combinations(rest, n-1)
        const combine = combis.map((v) => [fixed, ...v])
        result.push(...combine)
        
    })
    return result
}

function solution(numbers) {
    // n개씩 뽑아서 만들수있는 수의 합 리스트
    let res = combinations(numbers, 2)
    return [...new Set(res.map((lst, idx) => lst[0] + lst[1]).sort((a, b) => a-b))]
    
}