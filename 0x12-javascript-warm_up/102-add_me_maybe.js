#!/usr/bin/node

// Increments and calls a function

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
