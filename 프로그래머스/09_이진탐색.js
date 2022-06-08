const array = [1, 1, 5, 124, 400, 599, 1004, 2876, 8712]

function binarySearch(array, findValue) {
    let left = 0;
    let right = array.length -1;
    let mid = Math.floor((left + right) / 2)

    while (left < right) {
        if (array[mid] === findValue) {
            return mid
        }

        // 찾는값이 중간값보다 크면 
        if (array[mid] < findValue) {
            // left 이동
            left = mid + 1
        } else {
            // 아니면 right 이동
            right = mid - 1
        }

        mid = Math.floor((left + right) / 2)
    }

    return -1
}