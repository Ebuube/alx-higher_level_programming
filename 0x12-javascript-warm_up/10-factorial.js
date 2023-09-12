#!/usr/bin/node

// Add

const args = process.argv.slice(2);
// argv[0] -> interpreter
// argv[1] -> program

const num = parseInt(args[0]);
console.log(factorial(num));

function factorial (a) {
  // find the factorial of a number recursively
  if (isNaN(a) || a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
