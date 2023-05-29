#!/usr/bin/node

// require the file server
const fs = require('fs');

// Fetch command line arguments
const cmdLineArgs = process.argv.slice(2);

write(cmdLineArgs[2], concat(cmdLineArgs[0], cmdLineArgs[1]));

/*
 * concatenate two or more files and returns the combination
 */
function concat (...files) {
  let content = '';

  for (const file of files) {
    if (file === undefined) {
      console.log('Error (concat):\tfile name missing');
      console.log(`files[${files.indexOf(file)}]:\t${file}`);
      return undefined;
    }
  }
  for (const file of files) {
    content += fs.readFileSync(file).toString();
  }
  return content;
}

/*
 * write strings from srcText to destFile
 */
function write (destFile, srcText) {
  if (destFile === undefined || srcText === undefined) {
    console.log('Error (write):\tdestination and/or source files missing');
    return undefined;
  }
  fs.writeFileSync(destFile, srcText);
}
