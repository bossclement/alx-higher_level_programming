#!/usr/bin/nodejs

const Parent = require('./5-square');

class Square extends Parent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let h = 0; h < this.height; h++) {
      console.log(`${c}`.repeat(this.width));
    }
  }
}

module.exports = Square;
