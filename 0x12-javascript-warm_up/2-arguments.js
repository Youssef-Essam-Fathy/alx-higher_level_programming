#!/usr/bin/node
const countargv = process.argv.length;
if (countargv < 3) {
  console.log('No argument');
} else if (countargv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
