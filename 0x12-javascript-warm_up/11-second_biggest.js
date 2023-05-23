#!/usr/bin/node

// fetch cmd line args and remove the first two args
const cmdLineArgs = process.argv.slice(2);

const myList = cmdLineArgs.map(x => parseInt(x));

if (isNaN(myList[0]) || isNaN(myList[1])) {
  console.log(0);
} else {
  console.log(secondBiggest(myList));
}

// find the second biggest integer in a list

function secondBiggest (list) {
  // sort the list in descending order
  const sorted = list.sort((a, b) => b - a);
  // return the second element in the list
  return sorted[1];
}
