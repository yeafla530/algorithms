// array
const arr = []
console.log(arr);

arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
arr.push(5)
console.log(arr) // [1, 2, 3, 4 ,5]

arr["string"] = 10
arr[false] = 0
console.log(arr) // [1, 2, 3, 4, 5: 10, false: 0]
console.log(arr.length) // 5

arr[5] = 5
console.log(arr.length) // 6
console.log(arr) // [ 1, 2, 3, 4, 5, 5, string: 10, false: 0 ]


