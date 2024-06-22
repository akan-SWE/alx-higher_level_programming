#!/usr/bin/node

// increments and calls a function.
exports.addMeMaybe = (number, theFunction) => {
  theFunction(number + 1);
};
