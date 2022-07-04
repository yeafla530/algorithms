// 소수 : 1또는 자기 자신만을 약수로 가지는 수

// 효율적인 방법은?

//1. 1과 자기 자신을 제외한 수를 루프를 돌며 나눠보기 (2 ~ N-1)
// 느려서 코테에서 쓰이지 않음

function is_prime(num) {
    for (let i = 2; i < num; i+= 1) {
        if (num % i == 0) {
            return false
        }
    }

    return true;
}

// 2. 그 어떤 소수도 N의 제곱근보다 큰 수로 나눠지지 않는 다는 점 이용 (1번 개선)
// 시간 복잡도 O(sqrt(n))

function is_prime2(num) {
    for (let i = 2; i*i <= num; i+=1) {
        if (num % i == 0) {
            return false
        }
    }

    return true
}

//3. 에라토스테네스의 체
// O(n log log n)
function get_primes(num) {
    const prime = [false, false, ...Array(num - 1).fill(true)]
    console.log(prime)
    for (let i = 2; i *i <= num; i+=1) {
        if (prime[i]) {
            // i의 배수 for문으로 돌리기
            for (let j = i * 2; j <= num; j += i) {
                console.log('i, j', i, j)
                prime[j] = false
            }
        }
    }
    
    return prime.filter(Boolean);
}

// num = 11 이면

// i, j 2 4
// i, j 2 6
// i, j 2 8
// i, j 2 10
// i, j 3 6
// i, j 3 9