#!/usr/bin/node
/** searches the second biggest integer in the list of arguments. */
const argsString = process.argv.slice(2);
if (!argsString.length || argsString.length === 1) {
  console.log('0');
} else {
  // Convert each element to integers
  const argsInt = argsString.map(element => parseInt(element));
  // Sort the arrary of integers in desending order
  argsInt.sort(function (a, b) {
    return b - a;
  });
  console.log(argsInt[1]); // The second integer is the second largest
}
