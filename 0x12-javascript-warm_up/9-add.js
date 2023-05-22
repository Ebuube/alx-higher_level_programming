#!/usr/bin/node

// fetch cmd line arguments and strip of the first two arguments
const cmdLineArgs = process.argv.slice(2);

const first = parseInt(cmdLineArgs[0]);
const second = parseInt(cmdLineArgs[1]);

if (isNaN(first) || isNaN(second)) {
  console.log(NaN);
} else {
  console.log(add(first, second));
}

function add (a, b) {
  // add two integers
  return (a + b);
}
