#!/usr/bin/node
const Sqre = require('./5-square.js');
class Square extends Sqre {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        if (c !== undefined) {
          line += c;
        } else {
          line += 'X';
        }
      }
      console.log(line);
    }
  }
}

module.exports = Square;
