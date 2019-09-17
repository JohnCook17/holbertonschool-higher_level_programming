#!/usr/bin/node
const arg1 = process.argv[2];
const myInt = parseInt(arg1);
if (isNaN(myInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myInt);
}
