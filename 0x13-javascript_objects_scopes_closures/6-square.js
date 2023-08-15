#!/usr/bin/nodejs

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
