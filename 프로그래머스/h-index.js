function solution(citations) {
    citations = citations.sort(sorting);
    let i = 0;
    while(i + 1 <= citations[i]){
        i++;
    }
    return i;


    function sorting(a, b){
        return b - a;
    }
}