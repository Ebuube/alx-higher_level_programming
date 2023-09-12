#!/usr/bin/node

// arguments

const cmdLineArgs = process.argv.slice(2);
// Remove the first two arguments
// The first argument is the interpreter running the program
// The second argument is the absolute path of the program being executed
// The rest are the command line arguments supplied to the program

if (cmdLineArgs[0] === undefined) {
  console.log('No argument');
} else {
  console.log(cmdLineArgs[0]);
}
