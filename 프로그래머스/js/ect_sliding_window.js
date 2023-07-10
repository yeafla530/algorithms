function maxSumArr(arr, size) {
    let maxSum = 0;
    let tempSum = 0;
    if (arr.length < size) return null
    for (let i = 0; i < size; i++) {
        maxSum += arr[i]
    }
    tempSum = maxSum
    for (let i = size; i < arr.length; i ++) {
        tempSum = tempSum - arr[i - size] + arr[i]
        maxSum = Math.max(tempSum, maxSum)
    }
    return maxSum
}

console.log(maxSumArr([5, 100, 10000, 5, 300, 6], 3))