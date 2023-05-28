#!/usr/bin/node

// compute a new array

const list = require('./100-data.js').list;

compute(list);

function compute (list) {
  const newList = list.map((num, index) => num * index);
  console.log(list);
  console.log(newList);
}
