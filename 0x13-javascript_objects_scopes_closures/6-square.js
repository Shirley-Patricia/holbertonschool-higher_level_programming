#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let size;
    let j;

    for (size = 0; size < this.height; size++) {
      let row = '';
      for (j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
