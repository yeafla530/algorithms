function solution(s) {
    var answer = '';
    let arr = s.split(" ")
    
    let minNum = 987654321
    let maxNum = -987654321
    for (let i = 0; i < arr.length; i++) {
        if (minNum > parseInt(arr[i])) {
            minNum = parseInt(arr[i]) 
        }
        
        if (maxNum < parseInt(arr[i])) {
            maxNum = parseInt(arr[i]) 
            
        }
    }
    answer += String(minNum)
    answer += " "
    answer += String(maxNum)
    return answer;
}

function solution(s) {
    let answer = ""
    let arr = s.split(" ")
    
    return Math.min(...arr) + " " + Math.max(...arr)
}