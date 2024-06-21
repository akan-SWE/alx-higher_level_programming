#!/usr/bin/node

/**
 * Rectangle Defines a rectangle, ensures width and height are
 * positive integers otherwise an empty object is created.
 *
 * print() Prints the rectangle.
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
