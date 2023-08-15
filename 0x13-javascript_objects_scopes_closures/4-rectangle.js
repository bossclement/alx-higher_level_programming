#!/usr/bin/nodejs
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let h = 0; h < this.height; h++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    for (let w = 0; w < this.width; w++) {
      console.log('X'.repeat(this.height));
    }
  }

  double () {
    for (let h = 0; h < this.height * 2; h++) {
      console.log('X'.repeat(this.width * 2));
    }
  }
}

module.exports = Rectangle;
