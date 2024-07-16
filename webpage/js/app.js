// Demonstrate var, let, and const

// var example
console.log("var example:");
var x = 10;
console.log("outer x:", x);
if (true) {
  var x = 20;
  console.log("inner x:", x);
}
console.log("outer x again:", x); // outputs 20, because var has function scope

// let example
console.log("\nlet example:");
let y = 10;
console.log("outer y:", y);
if (true) {
  let y = 20;
  console.log("inner y:", y);
}
console.log("outer y again:", y); // outputs 10, because let has block scope

// const example
console.log("\nconst example:");
const z = 10;
console.log("z:", z);
try {
  z = 20; // TypeError: Assignment to constant variable.
} catch (error) {
  console.log("Error:", error.message);
}

// const with object example
console.log("\nconst with object example:");
const person = { name: 'John' };
console.log("person:", person);
person.name = 'Jane'; // allowed, person object is mutated
console.log("person after mutation:", person);
try {
  person = { name: 'Bob' }; // TypeError: Assignment to constant variable.
} catch (error) {
  console.log("Error:", error.message);
}