#!/usr/bin/node

// How many completed?
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
  console.log(`Usage: ${scriptName} <url> <filename>`);
  process.exit(exitFailure);
}

// const url = 'https://jsonplaceholder.typicode.com/todos';
const url = cmdLineArgs[0];
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  // console.log(body.toString());
  const tasks = JSON.parse(body);

  const users = new Map(); // id: <number of completed tasks
  for (const task of tasks) {
    if (users.has(task.userId) && task.completed === true) {
      users.set(task.userId, users.get(task.userId) + 1);
    } else if (!users.has(task.userId)) {
      users.set(task.userId, 0);
    }
  }

  // console.log(users); // test
  console.log(users); // test
});
