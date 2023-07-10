function solution(s) {
    let ans = ''
    var arr = [];
    arr = s.split(' ')
    console.log(arr)
    for (let i = 0; i < arr.length; i++) {
        let first = arr[i][0] ? arr[i][0].toUpperCase() : ''
        let remain = arr[i] ? arr[i].slice(1, arr[i].length).toLowerCase() : ''
        
        // console.log(first, remain)
        ans += first + remain
        if (i != arr.length-1) {
            ans += ' '
        }
        
    }
    
    return ans
}