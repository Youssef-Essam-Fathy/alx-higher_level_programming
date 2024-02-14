#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newlist = list.map((value, index) => value * index);
console.log(newlist);
