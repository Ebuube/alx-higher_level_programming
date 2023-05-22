#!/usr/bin/node

// I love C

const cmdLineArgs = process.argv.slice(2);
// remove first two arguments

const x = parseInt(cmdLineArgs[0]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
