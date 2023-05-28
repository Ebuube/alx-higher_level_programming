#!/usr/bin/node

// Fetch data
const dict = require('./101-data.js').dict;

console.log(sorted(dict));

function sorted (dict = {}) {
  const ids = [];
  // Fetch the ids
  for (const value of Object.values(dict)) {
    if (ids.includes(value) === false) {
      ids.push(value);
    }
  }

  // Fill new dictionary
  const newDict = {};
  for (const id of ids) {
    newDict[id] = (Object.keys(dict)).filter(key => dict[key] === id);
  }

  return newDict;
}
