#!/usr/bin/node

// Number Conversion

exports.converter = function (newBase) {
  return function (number) {
    return number.toString(newBase);
  };
};
