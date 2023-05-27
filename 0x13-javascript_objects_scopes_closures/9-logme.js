#!/usr/bin/node

// Print the number of arguments already printed and the new argument value

exports.logMe = function (item) {
  if (exports.logMe.count === undefined) {
    exports.logMe.count = 0;
  }
  console.log(`${exports.logMe.count}: ${item}`);
  exports.logMe.count += 1;
};
