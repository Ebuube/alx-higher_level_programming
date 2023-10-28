#!/usr/bin/node

// Loripsum
//
const request = require('request');
const fs = require('fs');

const scriptName = process.argv[1];
const cmdLineArgs = process.argv.slice(2);
// Remove the first two arguments
// The first argument is the interpreter running the program
// The second argument is the absolute path of the program being executed
// The rest are the command line arguments supplied to the program

const exitFailure = 1;
if (cmdLineArgs.length !== 2) {
  console.log(`Usage: ${scriptName} <url> <filename>`);
  process.exit(exitFailure);
}

// const endPoint = 'https://swapi-api.alx-tools.com/api/films/';
const url = cmdLineArgs[0];
const filename = cmdLineArgs[1];
request.get(url).pipe(fs.createWriteStream(filename));
