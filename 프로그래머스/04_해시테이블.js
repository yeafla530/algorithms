// 1:1 관계도 ex ) 학생부
// javascript Array == Object == Hash Table


// Object
const table = {};
table["key"] = 100;
table["key2"] = "Hello"
console.log(table) // { key: 100, key2: 'Hello' }
console.log(table["key"]) // 100
delete table["key"]
console.log(table["key"])

// Map
const table3 = new Mat();
table3.set("key", 100)
table3.set("key2", "Hello")
console.log(table3["key"]) //undefined
console.log(table3.get("key")) //100
const object = {a : 1};
table3.set(object, "A1")
console.log(table3.get(object)) //A1
table3.delete(object)
console.log(table3.get(object))
console.log(table3.keys())
console.log(table3.values())
table3.clear()
console.log(table3.values())



// Set
const table2 = new Set()
table2.add("key")
table2.add("key2")
console.log(table2.has("key"))
console.log(table2.has("key3"))
table2.delete("key2")
table2.add("key3")
console.log(table2) // { 'key', 'key3' }