#!/usr/bin/node

// Create a sentence

const cmdLineArgs = process.argv.slice(2); // remove first two arguments

console.log(cmdLineArgs[0] + ' is ' + cmdLineArgs[1]);
