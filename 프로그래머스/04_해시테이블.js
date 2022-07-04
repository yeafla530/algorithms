// 1:1 관계도 ex ) 학생부
// javascript Array == Object == Hash Table


// Object
// 재일 간단
// key값이 정수가 아닐경우 전부 string으로 바꿔버림
const table = {};
table["key"] = 100;
table["key2"] = "Hello"
console.log(table) // { key: 100, key2: 'Hello' }
console.log(table["key"]) // 100
delete table["key"]
console.log(table["key"])

// Map
// key값으로 object나 배열같은 복잡한 타입도 key로 사용할 수 있음 => 다양한 타입 넣을 수 있음

// 여러 편한 method 제공
// 순회를 편하게 할 수 있음
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
// key와 값이 동일하게 저장됨
// 일종의 집합 연산
// 중복된 내용 전부 제거할 때 사용
const table2 = new Set()
table2.add("key")
table2.add("key2")
console.log(table2.has("key"))
console.log(table2.has("key3"))
table2.delete("key2")
table2.add("key3")
console.log(table2) // { 'key', 'key3' }