#!/usr/bin/node

// fetch cmd line args and remove the first two of them
const cmdLineArgs = process.argv.slice(2);

const num = parseInt(cmdLineArgs[0]);

console.log(factorial(num));

function factorial (number) {
  if (number <= 0 || isNaN(number)) {
    return 1;
  }

  return (number * factorial(number - 1));
}
