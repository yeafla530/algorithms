// 같은 장르끼리 묶는다
// 묶인 노래들은 재생 순으로 정렬한다
// 노래를 2개까지 자르는 작업을 해야한다 

function solution(genres, plays) {
    let genreMap = new Map()
    genres
        .map((genre, idx) => [genre, plays[idx]])
        .forEach(([genre, play], idx) => {
            const data = genreMap.get(genre) || {total: 0, songs: []}
            genreMap.set(genre, {
                total:  data.total + play,
                songs: [...data.songs, {play, idx}]
                    .sort((a, b) => b.play - a.play)
                    .slice(0, 2)
                
            }) 
        })
    // console.log(genreMap)
    
    // console.log(genreMap.entries()) // key, value
    // console.log(test)
    return [...genreMap.entries()]
        .sort((a, b) => b[1].total - a[1].total)
        .flatMap(item => item[1].songs)
        .map(song => song.idx)
    
}