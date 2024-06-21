#!/usr/bin/node

/**
 * logMe prints the number of arguments already printed and the
 * new argument value
 */
let printedArgsCount = 0;
exports.logMe = function (item) {
  console.log(printedArgsCount + ':', item);
  printedArgsCount += 1;
};
