// Number data type
let num = 42;
let floatNum = 3.14;

// String data type
let str = "Hello, World!";
let singleQuoteStr = 'Hello, World!';

// Boolean data type
let isTrue = true;
let isFalse = false;

// Undefined data type
let notDefined;
console.log(notDefined); // undefined

// Null data type
let emptyValue = null;

// Symbol data type
let sym = Symbol('unique');

// BigInt data type
let bigInt = 1234567890123456789012345678901234567890n;

// Object data type
let obj = {
    name: "John Doe",
    age: 30
};

// Array data type
let arr = [1, 2, 3, 4, 5];

// Function data type
function greet() {
    console.log("Hello, World!");
}

// Output
console.log("Number:", num);
console.log("Float:", floatNum);
console.log("String:", str);
console.log("Single Quote String:", singleQuoteStr);
console.log("Boolean True:", isTrue);
console.log("Boolean False:", isFalse);
console.log("Undefined:", notDefined);
console.log("Null:", emptyValue);
console.log("Symbol:", sym);
console.log("BigInt:", bigInt);
console.log("Object:", obj);
console.log("Array:", arr);
greet(); // Hello, World!
