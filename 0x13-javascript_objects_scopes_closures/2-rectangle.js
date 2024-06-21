#!/usr/bin/node

/**
 * Rectangle - Defines a rectangle, ensures width and height are
 * positive integers otherwise an empty object is created.
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
