#!/usr/bin/node
const valargv = Number(process.argv[2]);
if (isNaN(valargv)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + valargv);
}
