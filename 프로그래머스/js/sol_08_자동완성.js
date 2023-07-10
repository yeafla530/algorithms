function makeTrie(words) {
    const root = {} // 먼저 루트 노드를 설정할 변수 만듦
    for (const word of words) { // trie 구서앟기 위한 루프 돌림
        let current = root; // 루트부터 시작
        for (const letter of word) { // 단어의 글자 하나씩 추출한 후
            if(!current[letter]) current[letter] = [0, {}] // 값을 넣는다. 리스트의 첫번째 값은 학습된 단어가 몇 개인지를 카운팅하고 두 번째 값은 트리 구조로 이용할 노드 값으로 사용한다.
            current[letter][0] = 1 + (current[letter][0] || 0); // 카운팅 위해 1더해준다
            current = current[letter][1] // current는 letter에 해당되는 노드로 이동

        }
    }

    return root
}

function solution(words) {
    let answer = 0;
    const trie = makeTrie(words); // Trie자료구조 만들기

    for (const word of words) {
        let count = 0;
        let current = trie; // 루트부터 시작
        
        for (const [index, letter] of [...word].entries()) {
            count += 1;
            if (current[letter][0] <= 1) { // 단어가 하나 이하로 남을 경우 종료
                break;
            }

            current = current[letter][1] // 다음 노드로 이동
        }
        answer += count // 카운팅을 더해준다
    }
    return answer
}

