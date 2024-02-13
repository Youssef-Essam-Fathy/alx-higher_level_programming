#!/usr/bin/node
/**
 * A class defining a rectangle with constructor
 * checking if the constructor params (w, h) are equal to 0
 * or negative value then create empty object
 */
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w <= 0 || h <= 0) {
      Object.create();
    }
  }
}
module.exports = Rectangle;
