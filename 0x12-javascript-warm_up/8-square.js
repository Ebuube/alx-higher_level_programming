#!/usr/bin/node

// Square

const cmdLineArgs = process.argv.slice(2);
// remove the first two arguments

const size = cmdLineArgs[0];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size; row++) {
    let line = '';

    for (let col = 0; col < size; col++) {
      line += 'X';
    }
    console.log(line);
  }
}
