#!/usr/bin/node

// Write me
//
const fs = require('fs');

const cmdLineArgs = process.argv.slice(2);
// Remove the first two arguments
// The first argument is the interpreter running the program
// The second argument is the absolute path of the program being executed
// The rest are the command line arguments supplied to the program

const exitFailure = 1;
if (cmdLineArgs.length !== 2) {
  console.log('Pass filename and string as argument to the script');
  console.log('Usage: ./0-readme.js <filename> "<input data>"');
  process.exit(exitFailure);
}
const filename = cmdLineArgs[0];
const data = cmdLineArgs[1];

fs.writeFile(filename, data, (err) => {
  if (err) {
    throw err;
  }
});
