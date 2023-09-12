#!/usr/bin/node
// Compute a new array
const list = require('./100-data').list;
const newList = list.map((x, y) => x * y);
console.log(list);
console.log(newList);
