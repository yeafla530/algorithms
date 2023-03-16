function solution(s) {
    let ans = [0, 0]
    
    while (s != '1') {
        s = s.split('')
        let n = s.filter(v => v === '1').length
        ans[0] ++
        ans[1] += s.length - n
        s = n.toString(2)
    }
    return ans
}