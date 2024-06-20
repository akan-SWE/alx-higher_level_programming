#!/usr/bin/node
const argLength = process.argv.length;
let message;
switch (argLength) {
  case 2:
    message = 'No argument';
    break;
  case 3:
    message = 'Argument found';
    break;
  default:
    message = 'Arguments found';
}
console.log(message);
