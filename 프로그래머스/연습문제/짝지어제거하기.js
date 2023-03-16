function solution(s)
{
    var answer = -1;
    let stack = []
    for (const chr of s) {
        if (stack.length === 0) {
            stack.push(chr)
        } else if (stack[stack.length-1] === chr) {
            stack.pop()
        } else {
            stack.push(chr)
        }
    }
    
    console.log(stack)
    return stack.length ? 0 : 1;
}