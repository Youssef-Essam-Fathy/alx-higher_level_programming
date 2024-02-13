#!/usr/bin/node
const x = Number(process.argv[2]);

function facto (x) {
  if (x === 0 || x === 1) {
    return (1);
  } else {
    return (x * facto(x - 1));
  }
}
if (isNaN(x)) {
  console.log(1);
} else {
  console.log(facto(x));
}
