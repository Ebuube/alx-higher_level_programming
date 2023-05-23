#!/usr/bin/node

// fetch cmd line args and remove the first two args
const cmdLineArgs = process.argv.slice(2);

let myList = cmdLineArgs.map(x => parseInt(x));

if (isNaN(myList[0]) || isNaN(myList[1])) {
  console.log(0);
} else {
  console.log(second_biggest(cmdLineArgs));
}

/*
// complete this function
function second_biggest (list) {
}
*/
