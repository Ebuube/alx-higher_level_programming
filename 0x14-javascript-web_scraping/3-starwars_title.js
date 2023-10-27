#!/usr/bin/node

// Star wars movie title
//
const request = require('request');

const cmdLineArgs = process.argv.slice(2);
// Remove the first two arguments
// The first argument is the interpreter running the program
// The second argument is the absolute path of the program being executed
// The rest are the command line arguments supplied to the program

const exitFailure = 1;
if (cmdLineArgs.length !== 1) {
  console.log('Usage: ./2-statuscode <movie_id>"');
  process.exit(exitFailure);
}
const id = cmdLineArgs[0];
const endPoint = 'https://swapi-api.alx-tools.com/api/films/';
const url = endPoint + id.toString();
request.get(url, (err, response, body) => {
  if (err) {
    throw err;
  }

  const resJson = JSON.parse(body);
  console.log(`${resJson.title}`);
});
