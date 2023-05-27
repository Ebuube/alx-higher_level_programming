#!/usr/bin/node

// Class Rectangle

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  // print the rectangle
  print () {
    const displaySymbol = 'X';
    for (let y = 0; y < this.height; y++) {
      let display = '';
      for (let x = 0; x < this.width; x++) {
        display += displaySymbol;
      }
      console.log(display);
    }
  }

  // exchange the width and the height
  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  // multiply the width and height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
