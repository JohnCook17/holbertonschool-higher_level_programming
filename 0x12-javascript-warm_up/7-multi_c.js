#!/usr/bin/node
const arg1 = process.argv[2];
const myInt = parseInt(arg1);
if (isNaN(myInt)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  if (myInt > 0) {
    while (i < myInt) {
      console.log('C is fun');
      i++;
    }
  }
}
