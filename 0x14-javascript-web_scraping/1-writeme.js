#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const strToWrite = process.argv[3];

fs.writeFile(filePath, strToWrite, 'utf8', (err, data) => {
  if (err) {
    console.error(`{ Error: ${err.message}\n    errno: ${err.errno},\n    code: '${err.code}',\n    syscall: '${err.syscall}',\n    path: '${err.path}' }`);
  }
});
