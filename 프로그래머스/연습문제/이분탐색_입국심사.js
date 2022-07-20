function solution(n, times) {
    times.sorted
    let left = 1
    let right = times[times.length -1] * n
    let mid = Math.floor((left + right) / 2)
    let result = right
    while (left <= right) {
        let count = times.reduce((res, cur) => res += Math.floor(mid/cur), 0)
        console.log(left, right, mid, result, count)
        // count가 n보다 크거나 같다 => mid값이 크다
        if (count >= n) {
            result = Math.min(result, mid)
            right = mid - 1
            console.log(result, right, left)
        // count가 더 작을 때는 result값 조정 x 
        // 가장 값이 작을거기 때문에
        } else {
            left = mid + 1
        }
        mid = Math.floor((left + right)/2)
    }
    return result
    
    
    
}