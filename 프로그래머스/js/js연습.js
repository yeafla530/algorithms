let hash = new Map()

hash.set(1, 0)
hash.set(2, 0)
hash.set(3, 0)

hash.get(1)

hash.has(1)

hash.delete(1)

hash.size

for (let [key,value] of hash) {
    console.log(key, value)
}