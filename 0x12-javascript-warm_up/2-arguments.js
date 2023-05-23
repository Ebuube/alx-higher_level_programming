#!/usr/bin/node

// Arguments

const cmdLineArgs = process.argv.slice(2);
// remove the first two arguments
// The first argument is the interpreter running the program
// The second argument is the absolute path of the program being executed
// The rest are the command line arguments supplied to the program

if (cmdLineArgs[0] === undefined) {
  console.log('No argument');
} else if (cmdLineArgs[1] === undefined) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
