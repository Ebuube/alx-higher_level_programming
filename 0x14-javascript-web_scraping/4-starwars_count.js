#!/usr/bin/node

// Star wars Wedge Antilles - ID = 18
//
const request = require('request');

const scriptName = process.argv[1];
const cmdLineArgs = process.argv.slice(2);
// Remove the first two arguments
// The first argument is the interpreter running the program
// The second argument is the absolute path of the program being executed
// The rest are the command line arguments supplied to the program

const exitFailure = 1;
if (cmdLineArgs.length !== 1) {
  console.log(`Usage: ${scriptName} <https://swapi-api.alx-tools.com/api/films>`);
  process.exit(exitFailure);
}

// const endPoint = 'https://swapi-api.alx-tools.com/api/films/';
const endPoint = cmdLineArgs[0];
const url = endPoint;
const charId = 18; // ID for Wedge Antilles
request.get(url, (err, response, body) => {
  if (err) {
    throw err;
  }
  if (response.statusCode !== 200) {
    console.log(`status code: ${response.statusCode}`);
    return;
  }

  const resJson = JSON.parse(body);
  let count = 0;
  const films = resJson.results;
  for (const film of films) {
    const pplUrl = 'https://swapi-api.alx-tools.com/api/people';
    const user = pplUrl + '/' + charId + '/';
    for (const character of film.characters) {
      if (character === user) {
        count++;
      }
    }
  }
  console.log(`${count}`);
});
