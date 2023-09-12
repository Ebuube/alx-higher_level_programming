#!/usr/bin/node

// Add

const args = process.argv.slice(2);
// argv[0] -> interpreter
// argv[1] -> program

const a = parseInt(args[0]);
const b = parseInt(args[1]);

console.log(add(a, b));

// FUNCTION
function add (a, b) {
  // add two integers
  return (a + b);
}
