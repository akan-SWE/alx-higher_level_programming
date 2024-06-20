#!/usr/bin/node
/* prints x times “C is fun” */

const limit = parseInt(process.argv[2]);
if (isNaN(limit)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < limit; i++) {
    console.log('C is fun');
  }
}
