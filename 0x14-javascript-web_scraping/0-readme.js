#!/usr/bin/node

// README
//
const fs = require('fs');

const cmdLineArgs = process.argv.slice(2);
// Remove the first two arguments
// The first argument is the interpreter running the program
// The second argument is the absolute path of the program being executed
// The rest are the command line arguments supplied to the program

const exitFailure = 1;
if (cmdLineArgs.length !== 1) {
  console.log('Pass filename as argument to the script');
  console.log('Usage: ./0-readme.js <filename>');
  process.exit(exitFailure);
}
const filename = cmdLineArgs[0];

const fmt = 'utf-8';
const callBackFunc = (err, inputD) => {
  if (err) throw err;
  console.log(inputD.toString());
};
fs.readFile(filename, fmt, callBackFunc);
