#!/usr/bin/node
const { dict } = require('./101-data.js');

const newDict = {};
for (const value in dict) {
  const kay = dict[value];
  if (kay in newDict) {
    newDict[kay].push(value);
  } else {
    newDict[kay] = [value];
  }
}

console.log(newDict);
