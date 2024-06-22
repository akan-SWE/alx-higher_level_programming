#!/usr/bin/node

// array and computes a new array.
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((item, i, arr) => item * i));
