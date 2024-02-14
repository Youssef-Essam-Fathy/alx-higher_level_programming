#!/usr/bin/node
const fs = require('fs');
const filename = process.argv.slice(2);
const array = [];
for (let i = 0; i <= 1; i++) {
  array.push(fs.readFileSync(filename[i], 'utf-8'));
}
const finaltext = array.join('');
fs.writeFileSync(filename[2], finaltext);
