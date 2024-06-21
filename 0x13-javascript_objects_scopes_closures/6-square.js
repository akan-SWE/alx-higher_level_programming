#!/usr/bin/node
const BaseSquare = require('./5-square');
/**
 * Square Defines a square that extends Square from 5-square module
 *
 * charPrint(c) Prints a square using the character c
 */
class Square extends BaseSquare {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
