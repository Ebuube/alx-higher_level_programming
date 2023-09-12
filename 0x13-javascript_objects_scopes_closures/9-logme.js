#!/usr/bin/node
// Logs the number of arguments already printed
exports.logMe = function (item) {
  if (exports.logMe.count === undefined) {
    exports.logMe.count = 0;
  }
  console.log(`${exports.logMe.count}: ${item}`);
  exports.logMe.count++;
};
