#!/usr/bin/node
const args = process.argv.slice(2);
if (args <= 1) {
  console.log('0');
} else {
  const myArray = [];
  for (const i in args) {
    myArray.push(parseInt(args[i]));
  }
  const myIndex = myArray.indexOf(Math.max.apply(Math, myArray));
  if (myIndex > -1) {
    myArray.splice(myIndex, 1);
  }
  console.log(Math.max.apply(Math, myArray));
}
