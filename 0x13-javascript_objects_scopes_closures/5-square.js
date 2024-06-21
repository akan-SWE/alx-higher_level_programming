#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * Square Defines a square that extends from Rectangle
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
