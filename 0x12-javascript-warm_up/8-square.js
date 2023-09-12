#!/usr/bin/node

// Print a square

const args = process.argv.slice(2);
// argv[0] => interpreter
// argv[1] => executing program

const character = 'X';
const num = parseInt(args[0]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  let line = '';
  for (let row = 0; row < num; row++) {
    line += character;
  }

  for (let y = 0; y < num; y++) {
    console.log(line);
  }
}
