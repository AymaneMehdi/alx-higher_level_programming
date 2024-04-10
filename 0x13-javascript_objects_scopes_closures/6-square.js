#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js
const Squa = require('./5-square.js');
class Square extends Squa {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.height));
      } else {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
