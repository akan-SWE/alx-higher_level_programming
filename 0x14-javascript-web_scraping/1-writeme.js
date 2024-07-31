#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);

const filepath = argv[0];
const content = argv[1];

fs.writeFile(filepath, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
