#!/usr/bin/node
const arg1 = process.argv[2];
const myInt = parseInt(arg1);
const square = 'X';
if (isNaN(myInt)) {
  console.log('Missing size');
} else {
  let i = 0;
  if (myInt > 0) {
    while (i < myInt) {
      console.log(square.repeat(myInt));
      i++;
    }
  }
}
