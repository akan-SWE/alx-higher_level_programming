#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv.slice(2);

fs.readFile(filePath[0], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
