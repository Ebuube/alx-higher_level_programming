#!/usr/bin/node
// A rectangle class with a constructor that validates type of arguments
// and an instance method

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // print the rectangle using the character
  print () {
    let row = ''; // a row of symbols
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  // exchange the width and the height of the rectangle
  rotate () {
    const dummy = this.width;
    this.width = this.height;
    this.height = dummy;
  }

  // multiply the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
