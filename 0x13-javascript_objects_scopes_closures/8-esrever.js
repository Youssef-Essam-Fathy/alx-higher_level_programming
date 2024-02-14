#!/usr/bin/node
exports.esrever = function (list) {
  const li = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    li[j] = list[i];
    j++;
  }
  return li;
};
