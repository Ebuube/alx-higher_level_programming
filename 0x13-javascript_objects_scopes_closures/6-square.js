#!/usr/bin/node

// Fetch previous class and make a Subclass of class Square
class Square extends require('./5-square') {
  // print the suqare usng the character passed in argument 'c'
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let y = 0; y < this.height; y++) {
        let display = '';
        for (let x = 0; x < this.width; x++) {
          display += c;
        }
        console.log(display);
      }
    }
  }
}
module.exports = Square;
