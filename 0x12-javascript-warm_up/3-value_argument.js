#!/usr/bin/node

// Value of my Argument

const cmdLineArgs = process.argv.slice(2);
// remove first two arguments

if (cmdLineArgs[0] === undefined) {
  console.log('No argument');
} else {
  console.log(cmdLineArgs[0]);
}
