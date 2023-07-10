// 배열에 있는 값 모두 제곱 
// 최대한 각 요소 모두 골고루 처리하는것이 중요
//매 루프마다 가장 큰 작업 찾아서 처리
// 매번 큰 값 혹은 작은값을 알아야한다면 무조건 Heap을 사용하는것이 좋음

class MaxHeap {
    constructor() {
        this.heap = [null];
    }
  
    push(value) {
        this.heap.push(value);
        let currentIndex = this.heap.length - 1;
        let parentIndex = Math.floor(currentIndex / 2);
  
        while (parentIndex !== 0 && this.heap[parentIndex] < value) {
            const temp = this.heap[parentIndex];
            this.heap[parentIndex] = value;
            this.heap[currentIndex] = temp;
  
            currentIndex = parentIndex;
            parentIndex = Math.floor(currentIndex / 2);
        }
    }
  
    pop() {
        if (this.heap.length === 2) return this.heap.pop(); // 루트 정점만 남은 경우
  
        const returnValue = this.heap[1];
        this.heap[1] = this.heap.pop();
  
        let currentIndex  = 1;
        let leftIndex = 2;
        let rightIndex = 3;
        while (this.heap[currentIndex] < this.heap[leftIndex] || 
               this.heap[currentIndex] < this.heap[rightIndex]) {
            if (this.heap[leftIndex] < this.heap[rightIndex]) {
                const temp = this.heap[currentIndex];
                this.heap[currentIndex] = this.heap[rightIndex];
                this.heap[rightIndex] = temp;
                currentIndex = rightIndex;
            } else {
                const temp = this.heap[currentIndex];
                this.heap[currentIndex] = this.heap[leftIndex];
                this.heap[leftIndex] = temp;
                currentIndex = leftIndex;
            }
            leftIndex = currentIndex * 2;
            rightIndex = currentIndex * 2 + 1;
        }
  
        return returnValue;
    }
  }

function solution(no, works) {
    // 1. works의 합이 no보다 작으면 비용 0
    if (works.reduce((a,b) => a + b) <= no) {
        return 0
    } 

    const heap = new MaxHeap();
    for (const work of works) {
        heap.push(work)
    }

    for (let i = 0; i < no; i++) {
        heap.push(heap.pop() - 1)
    }

    return heap.heap.reduce((a, b) => a + b*b)

}