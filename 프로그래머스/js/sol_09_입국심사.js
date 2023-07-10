function solution(n, times) {
    const sortedTime = times.sort((a,b) => a - b)
    let left = 1
    let right = sortedTime[sortedTime.length - 1] * n // 맨 마지막값 * 인원수

    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        // 30 / 7 + 30 / 10 = 7명
        const count = times.reduce((acc, time) => acc + Math.floor(mid / time), 0)

        // 작으면 
        if (count < n) {
            left = mid + 1;
        } else {
            right = mid - 1
        }
    }

    // right보다 left가 작은수
    return left
}