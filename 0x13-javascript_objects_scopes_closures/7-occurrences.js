#!/usr/bin/node
// Count the number of occurrences of a number in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const num of list) {
    if (num === searchElement) {
      count++;
    }
  }
  return count;
};
