#!/usr/bin/node
// A square with a method - charPrint(c)

class Square extends require('./5-square') {
  charPrint (c) {
    let symbol = 'X';
    if (c === undefined) {
      symbol = 'X';
    } else {
      symbol = c;
    }
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += symbol;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
