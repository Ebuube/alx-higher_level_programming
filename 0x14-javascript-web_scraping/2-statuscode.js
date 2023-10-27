#!/usr/bin/node

// Status code
//
const request = require('request');

const cmdLineArgs = process.argv.slice(2);
// Remove the first two arguments
// The first argument is the interpreter running the program
// The second argument is the absolute path of the program being executed
// The rest are the command line arguments supplied to the program

const exitFailure = 1;
if (cmdLineArgs.length !== 1) {
  console.log('Pass filename and string as argument to the script');
  console.log('Usage: ./2-statuscode <url>"');
  process.exit(exitFailure);
}
const url = cmdLineArgs[0];

request.get(url, (err, response, body) => {
  if (err) {
    throw err;
  } else {
    // console.log(`response: ${response}`);
    console.log(`code: ${response.statusCode}`);
  }
});
