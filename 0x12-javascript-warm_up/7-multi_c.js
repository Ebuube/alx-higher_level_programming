#!/usr/bin/node

// I love C

const args = process.argv.slice(2);
// arg[0] => interpreter
// arg[1] => name of program being executed

const x = parseInt(args[0]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
