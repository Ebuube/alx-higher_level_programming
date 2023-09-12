#!/usr/bin/node
// A square class - inherits from a Rectangle class
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
