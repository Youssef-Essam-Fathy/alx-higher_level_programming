#!/usr/bin/node
const valargv = process.argv;
if (valargv[2]) {
  console.log(valargv[2]);
} else {
  console.log('No argument');
}
