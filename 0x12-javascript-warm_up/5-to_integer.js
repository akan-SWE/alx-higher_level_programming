#!/usr/bin/node
const args = process.argv.slice(2);

args[0] = parseInt(args);
if (isNaN(args[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args[0]);
}
