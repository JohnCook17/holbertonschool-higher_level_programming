#!/usr/bin/node

const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.height));
        i++;
      }
    }
  }
};
