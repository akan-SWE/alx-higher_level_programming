#!/usr/bin/node

/**
 * Rectangle Defines a rectangle, ensures width and height are
 * positive integers otherwise an empty object is created.
 *
 * print() Prints the rectangle.
 * rotate() swap width and height
 * double() multiple width and height by 2
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

  rotate () {
    const store = this.width;
    this.width = this.height;
    this.height = store;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
