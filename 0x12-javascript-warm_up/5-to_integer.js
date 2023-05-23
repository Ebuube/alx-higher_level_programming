#!/usr/bin/node

// An integer

const cmdLineArgs = process.argv.slice(2);
// remove the first two arguments

const number = parseInt(cmdLineArgs[0]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ', number);
}
