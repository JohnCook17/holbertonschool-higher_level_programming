#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const myInt = parseInt(arg1);
const myInt2 = parseInt(arg2);
const myInt3 = myInt + myInt2;
console.log(myInt3);
