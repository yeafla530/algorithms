function solution(babbling) {
    let df = [ "aya", "ye", "woo", "ma"];
    let res = 0;
    for(let w of babbling) {
        if(df.some(f => w.includes(f+f))) continue;

        let rest = 
           df.reduce((a, f) => a.replaceAll(f, ""), w);

        if (rest.length > 0) continue;

        res++;
    }

    return res;
}