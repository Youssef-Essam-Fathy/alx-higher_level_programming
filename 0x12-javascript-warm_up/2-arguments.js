#!/usr/bin/node
const { argv } = require('node:process');
if (process.argv[2] == null) {
  console.log('No argument');
}
else if (process.argv[2] == 'Best') {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}