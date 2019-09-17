#!/usr/bin/node
const arg1 = process.argv[2];
const myInt = parseInt(arg1);
function factorial (n) {
  return (n !== 1) ? n * factorial(n - 1) : 1;
}
console.log(factorial(myInt));
