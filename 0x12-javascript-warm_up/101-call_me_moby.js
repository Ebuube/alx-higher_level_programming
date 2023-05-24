#!/usr/bin/node

// Call me Moby

exports.callMeMoby = function (x, theFunction) {
  for (let count = 0; count < x; count++) {
    theFunction();
  }
};
