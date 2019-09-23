#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length;
  const myList = [];
  while (i > 0) {
    myList.push(list[i - 1]);
    i--;
  }
  return myList;
};
