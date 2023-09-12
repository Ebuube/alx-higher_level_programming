#!/usr/bin/node
// Reverse a list
exports.esrever = function (list) {
  const revList = [];
  const len = list.length;

  for (let x = len - 1; x >= 0; x--) {
    revList.push(list[x]);
  }
  return revList;
};
